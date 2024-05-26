
# Exam Script

## Description
I made this tool to help my current classmates and future students study for an exam.
This tool provides very basic linux exercises and it's also osuited for beginners looking to practice.

This repository contains an automation script written in Python that sets up various directories and files for an examination environment. The script is designed to automate the creation of necessary files, directories, and configurations to simulate a realistic exam setup.

## Features

- **Banner Display**: Displays a cool ASCII banner at the start of the script.
- **Directory Check**: Checks if the 'playground' directory exists, and recreates it if necessary.
- **File and Directory Setup**: Automates the creation of various directories and files required for the exam.
- **File Operations**: Moves, copies, and renames files to configure the system correctly.
- **Symbolic Links**: Creates symbolic links for directories.
- **Tarball Handling**: Compresses and decompresses tarball files.
- **User Management**: Adds a new user and assigns them to a specific group.
- **Network Configuration**: Generates a brief list of configured network interfaces.
- **Executable Listing**: Produces an ordered list of executable files in the system directories.

## Usage

1. Clone this repository.
   
    ```bash
   wget https://github.com/Kyyomaa/Linux-Exercises/blob/main/exam_script.py
    ```
3. Run the script using Python:

    ```bash
    python3 exam_script.py
    ```

## Requirements

- Python 3.x
- Necessary permissions to create directories, files, and manage users on the system.

## Author

Made with love from Kyoma
