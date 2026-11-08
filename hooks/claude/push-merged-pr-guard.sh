#!/bin/bash
payload=$(cat)
command=$(printf '%s' "$payload" | jq -r '.tool_input.command // ""')
push=$(printf '%s' "$command" | grep -oE '(^|[;&|][[:space:]]*)git[[:space:]]+push([[:space:]][^;&|]*)?' | head -1) || exit 0
[ -n "$push" ] || exit 0

target_dir=$(printf '%s' "$command" | sed -n 's/^[[:space:]]*cd[[:space:]]\{1,\}\([^&|;]*\).*/\1/p' | head -1 | xargs 2>/dev/null)
[ -n "$target_dir" ] && [ -d "$target_dir" ] && cd "$target_dir"
git rev-parse --show-toplevel >/dev/null 2>&1 || exit 0

args=$(printf '%s' "$push" | sed -E 's/.*git[[:space:]]+push//' | tr ' ' '\n' | grep -v '^-' | grep -v '^$')
refspec=$(printf '%s\n' "$args" | sed -n '2p')
branch=${refspec##*:}
[ -z "$branch" ] || [ "$branch" = "HEAD" ] && branch=$(git rev-parse --abbrev-ref HEAD)
case "$branch" in staging|master|main) exit 0 ;; esac

states=$(gh pr list --head "$branch" --state all --json state,url --jq '.[] | "\(.state) \(.url)"' 2>/dev/null) || exit 0
printf '%s\n' "$states" | grep -q '^OPEN ' && exit 0
merged=$(printf '%s\n' "$states" | grep '^MERGED ' | head -1 | cut -d' ' -f2)
[ -n "$merged" ] || exit 0

echo "Push blocked: PR for branch $branch is already merged ($merged). Push to a new branch or to staging instead." >&2
exit 2
