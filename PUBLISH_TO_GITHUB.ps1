param(
  [string]$Repo = "inetconnector/testatika-small-research-replica",
  [switch]$Private
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  Write-Host "GitHub CLI (gh) is not installed."
  Write-Host "Install it with: winget install --id GitHub.cli"
  exit 1
}

gh auth status *> $null
if ($LASTEXITCODE -ne 0) {
  gh auth login
}

git status *> $null
if ($LASTEXITCODE -ne 0) {
  throw "Run this script from the repository root."
}

$visibility = if ($Private) { "--private" } else { "--public" }

gh repo view $Repo *> $null
if ($LASTEXITCODE -ne 0) {
  if ($Private) {
    gh repo create $Repo --private --source . --remote origin --push
  } else {
    gh repo create $Repo --public --source . --remote origin --push
  }
} else {
  git remote get-url origin *> $null
  if ($LASTEXITCODE -ne 0) {
    git remote add origin "https://github.com/$Repo.git"
  }
  git push -u origin HEAD
  git push origin --tags
}

Write-Host "Published: https://github.com/$Repo"
