#!/bin/bash

# Check if the virtual environment already exists
if [ ! -d "backend/venv" ]; then
    echo "Creating a Python 3.10 virtual environment..."
    python3.10 -m venv backend/venv
fi

# Activate the virtual environment
source backend/venv/bin/activate

# Ensure dependencies are up to date
pip install --no-cache-dir -r backend/requirements.txt

# Set environment variables (if needed)
export PYTHONWARNINGS="default"

# Run the Flask backend in the background
backend/venv/bin/python backend/app.py &

# Run the Tauri frontend
npm run tauri dev
