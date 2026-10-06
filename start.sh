#!/bin/bash

echo "🦊 Starting FoxSD AI Server..."

if [ ! -d "venv" ]; then
  echo "Virtual environment not found. Running setup..."
  bash setup.sh
fi

source venv/bin/activate
python main.py
