#!/usr/bin/env bash
set -euo pipefail
REPO="${1:-inetconnector/testatika-small-research-replica}"

if ! command -v gh >/dev/null; then
  echo "Install GitHub CLI first: https://cli.github.com/"
  exit 1
fi

gh auth status >/dev/null 2>&1 || gh auth login

if ! gh repo view "$REPO" >/dev/null 2>&1; then
  gh repo create "$REPO" --public --source . --remote origin --push
else
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$REPO.git"
  git push -u origin HEAD
  git push origin --tags
fi

echo "Published: https://github.com/$REPO"
