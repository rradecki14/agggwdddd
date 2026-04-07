#!/usr/bin/env bash
# Navigate to script directory to ensure relative paths work
cd "$(dirname "$0")"

pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}
