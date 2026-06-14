#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-/Users/ganxuanzhi/skills}"

printf 'Skills root: %s\n\n' "$ROOT"
find "$ROOT" \
  -path "$ROOT/_management" -prune -o \
  -name SKILL.md -type f -print |
  sort |
  while IFS= read -r file; do
    name="$(awk -F': *' '/^name:/ {print $2; exit}' "$file" | tr -d '"')"
    desc="$(awk '
      /^description:[[:space:]]*>-/ {
        in_desc=1
        next
      }
      /^description:/ {
        sub(/^description:[[:space:]]*/, "")
        print
        exit
      }
      in_desc && /^[[:space:]]+[A-Za-z0-9("'\''[:space:][:punct:]]/ {
        sub(/^[[:space:]]+/, "")
        printf "%s ", $0
        next
      }
      in_desc && /^[A-Za-z_-]+:/ {
        exit
      }
    ' "$file")"
    status_file="$(dirname "$file")/STATUS.md"
    if [[ -f "$status_file" ]]; then
      status="has STATUS.md"
    else
      status="missing STATUS.md"
    fi
    printf '%s\n  path: %s\n  status: %s\n  description: %s\n\n' "${name:-unknown}" "$file" "$status" "${desc:-see SKILL.md}"
  done
