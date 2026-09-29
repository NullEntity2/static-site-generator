#!/usr/bin/env bash
set -e

export PYTHONPATH="src${PYTHONPATH:+:$PYTHONPATH}"

if [[ "$1" == "--debug" ]]; then
    uv run python -m debugpy --listen 5678 --wait-for-client -m unittest discover -s test
else
    uv run python -m unittest discover -s test
fi
