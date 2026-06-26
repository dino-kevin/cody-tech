#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Creating virtual environment 'myenv'..."
python3 -m venv myenv

echo "Activating 'myenv'..."
source myenv/bin/activate

echo "Installing ipykernel..."
# Upgrade pip first to avoid warnings, then install ipykernel
pip install --upgrade pip
pip install ipykernel

echo "Registering the kernel with Jupyter..."
python -m ipykernel install --user --name=myenv --display-name="Python (myenv)"

echo ""
echo "✅ Setup complete! The kernel is registered."
echo "Note: You are now working inside 'myenv'."
