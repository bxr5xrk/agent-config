#!/usr/bin/env node

import { access, lstat, mkdir, readFile, readlink, readdir, rename, symlink, unlink, writeFile } from "node:fs/promises";
import { homedir } from "node:os";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const managedHome = resolve(process.env.AGENT_CONFIG_HOME || homedir());
const statePath = join(managedHome, ".config", "agent-config", "state.json");
const targetRoots = {
  codex: join(managedHome, ".agents", "skills"),
  claude: join(managedHome, ".claude", "skills"),
};
const safeName = /^[a-z0-9][a-z0-9-]*$/;

function usage() {
  return `Usage: pnpm sync --profile <personal|work> --target <codex|claude> [--apply|--check]

Without a mode flag, the command only previews changes.`;
}

function parseArgs(argv) {
  const options = { mode: "preview" };

  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];

    if (argument === "--profile" || argument === "--target") {
      const value = argv[index + 1];
      if (!value || value.startsWith("--")) {
        throw new Error(`Missing value for ${argument}`);
      }
      options[argument.slice(2)] = value;
      index += 1;
      continue;
    }

    if (argument === "--apply" || argument === "--check") {
      const nextMode = argument.slice(2);
      if (options.mode !== "preview") {
        throw new Error("Choose only one of --apply or --check");
      }
      options.mode = nextMode;
      continue;
    }

    if (argument === "--help" || argument === "-h") {
      options.help = true;
      continue;
    }

    throw new Error(`Unknown argument: ${argument}`);
  }

  return options;
}

async function pathStatus(path) {
  try {
    return await lstat(path);
  } catch (error) {
    if (error.code === "ENOENT") return null;
    throw error;
  }
}

async function loadJson(path, fallback) {
  try {
    return JSON.parse(await readFile(path, "utf8"));
  } catch (error) {
    if (error.code === "ENOENT") return fallback;
    throw error;
  }
}

async function loadProfile(name) {
  if (!safeName.test(name)) {
    throw new Error(`Invalid profile name: ${name}`);
  }

  const path = join(repoRoot, "profiles", `${name}.json`);
  const profile = await loadJson(path, null);
  if (!profile) throw new Error(`Unknown profile: ${name}`);
  if (profile.name !== name || !Array.isArray(profile.scopes) || profile.scopes.length === 0) {
    throw new Error(`Invalid profile: ${path}`);
  }

  return profile;
}

async function collectSkills(profile) {
  const skills = new Map();

  for (const scope of profile.scopes) {
    if (!safeName.test(scope)) {
      throw new Error(`Invalid scope name: ${scope}`);
    }

    const scopeRoot = join(repoRoot, "skills", scope);
    const entries = await readdir(scopeRoot, { withFileTypes: true });
    for (const entry of entries) {
      if (!entry.isDirectory()) continue;

      const source = join(scopeRoot, entry.name);
      await access(join(source, "SKILL.md"));
      if (skills.has(entry.name)) {
        throw new Error(`Duplicate skill '${entry.name}' in scopes '${skills.get(entry.name).scope}' and '${scope}'`);
      }
      skills.set(entry.name, { name: entry.name, scope, source });
    }
  }

  return new Map([...skills.entries()].sort(([left], [right]) => left.localeCompare(right)));
}

function resolveLink(destination, link) {
  return resolve(dirname(destination), link);
}

async function makePlan(target, desired, state) {
  const targetRoot = targetRoots[target];
  const previous = state.targets?.[target]?.skills || {};
  const actions = [];

  for (const [name, source] of Object.entries(previous)) {
    if (!safeName.test(name) || typeof source !== "string") {
      throw new Error(`Invalid managed state for target '${target}'`);
    }
  }

  for (const skill of desired.values()) {
    const destination = join(targetRoot, skill.name);
    const status = await pathStatus(destination);

    if (!status) {
      actions.push({ type: "create", ...skill, destination });
      continue;
    }

    if (!status.isSymbolicLink()) {
      actions.push({ type: "conflict", ...skill, destination, reason: "destination is not a symlink" });
      continue;
    }

    const currentSource = resolveLink(destination, await readlink(destination));
    if (currentSource === skill.source) {
      const trackedSource = previous[skill.name];
      const type = trackedSource && resolve(trackedSource) === skill.source ? "ok" : "adopt";
      actions.push({ type, ...skill, destination });
      continue;
    }

    if (previous[skill.name] && resolve(previous[skill.name]) === currentSource) {
      actions.push({ type: "replace", ...skill, destination });
      continue;
    }

    actions.push({ type: "conflict", ...skill, destination, reason: `symlink points to ${currentSource}` });
  }

  for (const [name, previousSource] of Object.entries(previous)) {
    if (desired.has(name)) continue;

    const destination = join(targetRoot, name);
    const status = await pathStatus(destination);
    if (!status) {
      actions.push({ type: "forget", name, destination, source: previousSource });
      continue;
    }

    if (status.isSymbolicLink()) {
      const currentSource = resolveLink(destination, await readlink(destination));
      if (currentSource === resolve(previousSource)) {
        actions.push({ type: "remove", name, destination, source: previousSource });
        continue;
      }
    }

    actions.push({
      type: "conflict",
      name,
      destination,
      source: previousSource,
      reason: "previously managed destination was changed externally",
    });
  }

  return actions.sort((left, right) => left.name.localeCompare(right.name));
}

function printPlan(mode, profile, target, actions) {
  console.log(`${mode.toUpperCase()} profile=${profile.name} target=${target}`);
  for (const action of actions) {
    const label = action.type.toUpperCase().padEnd(8);
    const source = action.source ? ` -> ${relative(repoRoot, action.source) || "."}` : "";
    const reason = action.reason ? ` (${action.reason})` : "";
    console.log(`${label} ${action.destination}${source}${reason}`);
  }
}

async function saveState(state) {
  await mkdir(dirname(statePath), { recursive: true });
  const temporaryPath = `${statePath}.${process.pid}.tmp`;
  await writeFile(temporaryPath, `${JSON.stringify(state, null, 2)}\n`, { mode: 0o600 });
  await rename(temporaryPath, statePath);
}

async function applyPlan(profile, target, desired, state, actions) {
  const conflicts = actions.filter((action) => action.type === "conflict");
  if (conflicts.length > 0) {
    throw new Error("Refusing to overwrite paths not safely managed by agent-config");
  }

  await mkdir(targetRoots[target], { recursive: true });
  for (const action of actions) {
    if (action.type === "remove" || action.type === "replace") {
      await unlink(action.destination);
    }
    if (action.type === "create" || action.type === "replace") {
      await symlink(action.source, action.destination, "dir");
    }
  }

  state.version = 1;
  state.targets ||= {};
  state.targets[target] = {
    profile: profile.name,
    skills: Object.fromEntries([...desired.values()].map((skill) => [skill.name, skill.source])),
  };
  await saveState(state);
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  if (options.help) {
    console.log(usage());
    return;
  }
  if (!options.profile || !options.target) {
    throw new Error(`${usage()}\n\nBoth --profile and --target are required.`);
  }
  if (!(options.target in targetRoots)) {
    throw new Error(`Unknown target: ${options.target}`);
  }

  const profile = await loadProfile(options.profile);
  const desired = await collectSkills(profile);
  const state = await loadJson(statePath, { version: 1, targets: {} });
  const actions = await makePlan(options.target, desired, state);
  printPlan(options.mode, profile, options.target, actions);

  const conflicts = actions.filter((action) => action.type === "conflict");
  if (options.mode === "check") {
    const mismatches = actions.filter((action) => action.type !== "ok");
    if (state.targets?.[options.target]?.profile !== profile.name) {
      throw new Error(`Check failed because target '${options.target}' is not recorded with profile '${profile.name}'`);
    }
    if (mismatches.length > 0) {
      throw new Error(`Check failed with ${mismatches.length} mismatch(es)`);
    }
    console.log(`OK ${desired.size} skill(s) are synchronized.`);
    return;
  }

  if (options.mode === "apply") {
    await applyPlan(profile, options.target, desired, state, actions);
    console.log(`APPLIED ${desired.size} skill(s).`);
    return;
  }

  if (conflicts.length > 0) process.exitCode = 1;
}

main().catch((error) => {
  console.error(`ERROR ${error.message}`);
  process.exitCode = 1;
});
