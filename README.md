# Automated Directory Organizer

A lightweight Python script that automates directory cleanup by sorting miscellaneous files into dedicated categorized folders based on their extensions.

## Features
- Dynamic routing using an extension map (Dictionary-based architecture).
- Prevent script self-displacement using dynamic basename evaluation.
- Follows DRY (Don't Repeat Yourself) principles for clean and maintainable code.

## How It Works
The script scans the target directory, detects file extensions, creates appropriate folders (`Images`, `Documents`, `Videos`, etc.) if they don't exist, and safely moves the files.

## Usage
Simply place the script in the directory you want to clean up and run:
```bash
python test01.py
