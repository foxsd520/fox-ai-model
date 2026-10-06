#!/bin/bash

echo "🦊 Setting up FoxSD AI Environment..."

if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "\n✅ Setup complete!"
echo "\nTo start the server, run:"
echo "  source venv/bin/activate"
echo "  python main.py"
echo "\nThen open http://localhost:8000 in your browser."
