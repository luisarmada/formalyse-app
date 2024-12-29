#!/bin/bash
source backend/venv/bin/activate
pip install -r backend/requirements.txt
python3 backend/app.py &
# npm run tauri dev
npm run tauri dev