# sandboxPython


**sandboxPython** is a Python playground for learning and experimenting with various Python libraries and frameworks. It provides a safe space for developers at all levels to improve their programming skills and develop practical applications.


## Features

- **Experimentation**: Create new files and explore different code snippets.
- **Learning**: Utilize various Python libraries to understand their functionalities.
- **Practical Applications**: Build small projects to solidify your understanding of concepts.

## Directory Structure

This repository contains several Python scripts categorized by their functionality:

### 1. Basic Games and Utilities

- **rollDice.py**
  - **Description**: A simple program that simulates rolling dice, returning results based on the number of dice and the sides specified. Great for learning randomness and control flow in Python.

- **rps-rock-paper-scissors.py**
  - **Description**: Implements the classic game of Rock, Paper, Scissors. This project demonstrates user input handling and conditional logic.
  
- **version.py**
  - **Description**: version.py generates a version string representing the current state of the application based on the current week and year. 
  - This script provides a simple way to track the versioning of your applications and aids in maintaining clarity regarding the release timeline and updates. Ideal for developers looking to integrate versioning in their workflow or for educational purposes in understanding Python date and time manipulation.
  - The version format follows the convention KYYYY.QX.WW.X, where:
  - KYYYY: The current year (e.g., K2024).
  - QX: The quarter of the year (Q1, Q2, Q3, Q4).
  - WW: The ISO week number for the current week.
  - X: A patch version calculated as a multiple of 3 based on the current day of the week.

### 2. Translation Utilities

- **translator/**
  - **Directory Description**: Contains multiple scripts related to text translation functionalities.

  - **translator.py**
    - **Description**: A core script implementing the translation logic, which interacts with translation libraries or APIs.

### 3. Text-to-Speech Utilities

- **text2speech/**
  - **Directory Description**: Contains scripts for converting text to speech.

  - **text2speech.py**
    - **Description**: A primary script that uses libraries to take input text and convert it into spoken words, showcasing text processing and audio output capabilities.

## Getting Started

To get started with **sandboxPython**, follow these simple steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sandboxPython.git
   cd sandboxPython
   ```

2. Install Required Libraries: Make sure you have Python installed on your machine. You may need to install additional libraries based on the scripts you'll be using:

    ```bash
    pip install <library-name>
    ```
3. Run a Script: Choose a script you want to experiment with and run it:

```bash
python rollDice.py
```

## Contributing
Contributions are welcome! Feel free to create new scripts, modify existing ones, or suggest enhancements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Acknowledge any resources, libraries, or inspirations that helped in the development of this project.

- deep-translator
- langdetect
- gtts