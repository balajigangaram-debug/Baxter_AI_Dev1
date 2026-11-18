#!/usr/bin/env bash
set -euo pipefail
uv venv --python 3.12 .venv
uv sync --extra dev
cp -n .env.example .env
echo 'Environment ready. Run: uv run python -m baxter_ai'
