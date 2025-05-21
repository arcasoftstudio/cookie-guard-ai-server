#!/bin/bash

set -e
export DEBIAN_FRONTEND=noninteractive

echo "🔧 Installazione dipendenze di sistema base..."
apt update && apt install -y \
    git build-essential wget unzip python3-pip libgl1

echo "🐍 Installazione dipendenze Python..."
pip install --upgrade pip
pip install -r /workspace/requirements.txt

echo "📂 Avvio API AI CookieGuard..."
cd /workspace
uvicorn main:app --host 0.0.0.0 --port 8000
