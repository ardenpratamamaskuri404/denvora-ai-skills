#!/usr/bin/env bash
# Package the skill folder into dist/denvora-ai-skills.skill (a zip archive)
# and dist/denvora-ai-skills.zip, for uploading to Claude (Settings > Skills)
# or attaching to a GitHub Release.
#
# Usage: ./scripts/package-skill.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL_NAME="denvora-ai-skills"
SKILL_DIR="$ROOT/skills/$SKILL_NAME"
DIST="$ROOT/dist"

if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
  echo "Error: $SKILL_DIR/SKILL.md not found." >&2
  exit 1
fi

if ! command -v zip >/dev/null 2>&1; then
  echo "Error: 'zip' is not installed. Install it (e.g. 'sudo apt install zip') and retry." >&2
  exit 1
fi

mkdir -p "$DIST"
rm -f "$DIST/$SKILL_NAME.skill" "$DIST/$SKILL_NAME.zip"

# Zip with the skill folder as the top-level entry.
(cd "$ROOT/skills" && zip -rq "$DIST/$SKILL_NAME.zip" "$SKILL_NAME" -x "*.DS_Store")
cp "$DIST/$SKILL_NAME.zip" "$DIST/$SKILL_NAME.skill"

echo "Created:"
echo "  $DIST/$SKILL_NAME.skill"
echo "  $DIST/$SKILL_NAME.zip"
