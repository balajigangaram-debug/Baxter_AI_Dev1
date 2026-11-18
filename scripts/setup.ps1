$ErrorActionPreference = 'Stop'
uv venv --python 3.12 .venv
uv sync --extra dev
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
Write-Host 'Environment ready. Run: uv run python -m baxter_ai'
