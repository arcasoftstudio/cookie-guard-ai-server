#!/bin/bash

set -e
export DEBIAN_FRONTEND=noninteractive

echo "🔧 Installazione base: Python + pip"
apt update && apt install -y python3 python3-pip libgl1 libglib2.0-0

echo "🐍 Installazione dipendenze Python..."
pip3 install --upgrade pip
pip3 install -r /workspace/cookie-guard-ai-server/requirements.txt
pip3 install fastapi uvicorn pillow numpy ultralytics python-multipart

echo "🚀 Avvio FastAPI..."
cd /workspace/cookie-guard-ai-server
uvicorn main:app --host 0.0.0.0 --port 8000
