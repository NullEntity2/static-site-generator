#!/usr/bin/env bash
set -e

if [[ "$1" == "--debug" ]]; then
    uv run python -m debugpy --listen 5678 --wait-for-client -m unittest discover -s src
else
    uv run python -m unittest discover -s src
fi
