import assert from "node:assert/strict";
import { lstat, mkdir, mkdtemp, readlink, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import test from "node:test";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const script = join(repoRoot, "scripts", "sync.mjs");
const common = ["brainstorm", "grill-me", "grilling"];
const personal = ["backend", "build", "designer", "frontend", "onboarding"];

async function temporaryHome(t) {
  const path = await mkdtemp(join(tmpdir(), "agent-config-"));
  t.after(() => rm(path, { recursive: true, force: true }));
  return path;
}

function run(home, ...args) {
  return spawnSync(process.execPath, [script, ...args], {
    encoding: "utf8",
    env: { ...process.env, AGENT_CONFIG_HOME: home },
  });
}

async function assertLink(path, expected) {
  assert.equal((await lstat(path)).isSymbolicLink(), true);
  assert.equal(resolve(dirname(path), await readlink(path)), expected);
}

test("preview does not write files", async (t) => {
  const home = await temporaryHome(t);
  const result = run(home, "--profile", "personal", "--target", "codex");

  assert.equal(result.status, 0, result.stderr);
  await assert.rejects(lstat(join(home, ".agents")), { code: "ENOENT" });
});

test("applies and checks personal and work profiles", async (t) => {
  const home = await temporaryHome(t);
  let result = run(home, "--profile", "personal", "--target", "codex", "--apply");
  assert.equal(result.status, 0, result.stderr);

  for (const name of [...common, ...personal]) {
    const scope = common.includes(name) ? "common" : "personal";
    await assertLink(join(home, ".agents", "skills", name), join(repoRoot, "skills", scope, name));
  }

  result = run(home, "--profile", "personal", "--target", "codex", "--check");
  assert.equal(result.status, 0, result.stderr);

  result = run(home, "--profile", "work", "--target", "claude", "--apply");
  assert.equal(result.status, 0, result.stderr);
  for (const name of common) {
    await assertLink(join(home, ".claude", "skills", name), join(repoRoot, "skills", "common", name));
  }
});

test("switching a target profile removes only stale managed links", async (t) => {
  const home = await temporaryHome(t);
  let result = run(home, "--profile", "personal", "--target", "codex", "--apply");
  assert.equal(result.status, 0, result.stderr);

  const unrelated = join(home, ".agents", "skills", "unrelated", "SKILL.md");
  await mkdir(dirname(unrelated), { recursive: true });
  await writeFile(unrelated, "---\nname: unrelated\n---\n");

  result = run(home, "--profile", "work", "--target", "codex", "--apply");
  assert.equal(result.status, 0, result.stderr);
  for (const name of personal) {
    await assert.rejects(lstat(join(home, ".agents", "skills", name)), { code: "ENOENT" });
  }
  assert.equal((await lstat(dirname(unrelated))).isDirectory(), true);
});

test("refuses to overwrite an unmanaged destination", async (t) => {
  const home = await temporaryHome(t);
  const conflict = join(home, ".claude", "skills", "brainstorm");
  await mkdir(conflict, { recursive: true });

  const result = run(home, "--profile", "work", "--target", "claude", "--apply");
  assert.equal(result.status, 1);
  assert.match(result.stderr, /Refusing to overwrite/);
  assert.equal((await lstat(conflict)).isDirectory(), true);
});
