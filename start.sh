#!/bin/bash
echo "Avvio Cookie Guard AI Server..."
uvicorn main:app --host 0.0.0.0 --port 8000
