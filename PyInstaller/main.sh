#!/bin/bash

# Ensure you have PyInstaller installed
echo "Installing PyInstaller..."
pip install pyinstaller

# Define the Python file to convert
PYTHON_FILE="filename.py"

# Create a standalone executable
echo "Creating executable for $PYTHON_FILE..."
pyinstaller --onefile "$PYTHON_FILE"

# Completion message
echo "Done! Check the 'dist' folder for your executable."