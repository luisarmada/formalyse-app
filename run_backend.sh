#!/bin/bash
source backend/venv/bin/activate
pip install -r backend/requirements.txt
python3 backend/app.py