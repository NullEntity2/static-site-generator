#!/usr/bin/env bash
set -e

if [[ "$1" == "--debug" ]]; then
    uv run -m debugpy --listen localhost:5678 --wait-for-client src/main.py && cd public && python3 -m http.server 8888
else
    uv run src/main.py && cd public && python3 -m http.server 8888
fi