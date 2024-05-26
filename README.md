
# Exam Automation Script

## Description

This repository contains an automation script written in Python that sets up various directories and files for an examination environment. The script is designed to automate the creation of necessary files, directories, and configurations to simulate a realistic exam setup. Each function in the script performs a specific task, such as creating directories, writing README files, moving files, and creating symbolic links. The script ensures that all tasks are completed accurately and efficiently.

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

## Functions

### `banner`

Displays an ASCII banner to introduce the script.

### `dirCheck`

Checks if the 'playground' directory exists. If it does, it removes the old playground and creates a new one.

### `filler`

Creates a README.md file in a specified subdirectory with provided content.

### `alias`

Creates a README.md file in the 'Alias' directory with instructions on setting up an alias for listing files.

### `backup`

Creates a README.md file in the 'Backup' directory and sets up a 'foo' directory.

### `dove`

Creates a README.md file in the 'Dove' directory with instructions for using the `tree` command.

### `script`

Creates a README.md file in the 'Script' directory and a sample script file.

### `lista`

Creates a README.md file in the 'Lista' directory with instructions for listing executables.

### `configRete`

Creates a README.md file in the 'ConfigRete' directory with instructions for listing network interfaces.

### `fileTemp`

Creates a README.md file in the 'FileTemp' directory and several temporary files.

### `tarball`

Creates a README.md file in the 'Tarball' directory, creates a tarball, and then removes the original file.

### `traslochi`

Creates a README.md file in the 'Traslochi' directory and performs file move and copy operations.

### `link`

Creates a README.md file in the 'Link' directory and sets up a symbolic link.

### `rinomina`

Creates a README.md file in the 'Rinomina' directory and renames a file.

### `user`

Creates a README.md file in the 'User' directory with instructions for adding a user and assigning them to a group.

### `starter`

Calls all the above functions in sequence to set up the entire exam environment.

## Usage

1. Clone this repository.
2. Run the script using Python:

    ```bash
    python3 exam_script.py
    ```

## Requirements

- Python 3.x
- Necessary permissions to create directories, files, and manage users on the system.

## Author

Made with love from Kyoma

---

This script is designed to automate and simplify the setup of an exam environment, ensuring consistency and efficiency in preparing the necessary files and directories. It is a valuable tool for educators and administrators who need to prepare multiple exam environments quickly.
```
