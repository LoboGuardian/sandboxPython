###!/bin/bash

### Ensure you have PyInstaller installed
echo "Installing PyInstaller..."
pip install pyinstaller

### Define the Python file to convert
PYTHON_FILE="filename.py"

### Create a standalone executable
echo "Creating executable for $PYTHON_FILE..."
pyinstaller --onefile "$PYTHON_FILE"

### Additional Suggestions
echo "Additional Suggestions:"

### Testing suggestion
echo "1. Testing: Always run your .exe in a testing environment to ensure it's working as expected."
echo "   Check for any missing dependencies or other runtime errors."

### Custom Icon suggestion
echo "2. Custom Icon: To add an icon to your executable, use the --icon option:"
echo "   Example: pyinstaller --onefile --icon=myicon.ico $PYTHON_FILE"

### Hide Console Window suggestion
echo "3. Hide Console Window: To create a GUI application without showing a console window, use the --noconsole option:"
echo "   Example: pyinstaller --onefile --noconsole $PYTHON_FILE"

### Documentation reference
echo "4. Documentation: For more options and a better understanding, refer to the PyInstaller documentation:"
echo "   https://pyinstaller.readthedocs.io/en/stable/"

### Completion message
ehho "Done! Check the 'dist' folder for your executable." 