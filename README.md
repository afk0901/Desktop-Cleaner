

# 🧹 Desktop Organizer – Python Automation Tool

Tired of your cluttered Desktop?

**Desktop Organizer** is a simple yet powerful Python automation tool built for Windows that brings instant order to your chaos. It scans your Desktop and automatically moves files into folders based on file extensions — no clicks, no dragging, no nonsense.

Whether it's scattered PDFs, Word docs, Excel sheets, or plain text files, this script puts everything in its place. Clean workspace, clear mind.

## 🔹 Highlights
- Built in pure Python
- Packaged as `.exe` (runs without Python installed)
- Uses Windows Registry to detect Desktop (OneDrive-safe)
- Fully tested with 27 Pytest test cases
- Designed for extensibility and safety

## 🖥️ Desktop Organizer – Demo

A link to a 1 minute demo video demonstrating the functionality of 
the tool: https://youtu.be/pJ7ma_gBGZU 

## Current Features

Automatically sorts:
  - `.pdf` → `PDF Documents`
  - `.docx`, `.doc` → `Word Documents`
  - `.xlsx`, `.xls`, `.odt` → `Excel Documents`
  - `.txt` → `Text Documents`
- Resolves correct Desktop path (supports OneDrive and standard setups)
- Packaged as .exe – no Python needed for users

## How to install the project's dependencies

Run this command in the terminal: `pip install -r ./requirements.txt` and 
that should be it.

## How to run the tool

Download the .exe from the latest release in this repository or clone the repo and follow the instructions below.

The main entry file is desktop_organizer.py. Run it in your IDE or run this command inside the root directory of the project: 
`python desktop_organizer.py`. This command should start the tool.

## 🧪 Tests

This project includes automated tests to verify file movement behavior and handling edge cases.

The project uses Pytest for all it's tests. You can run the tests in your IDE or run them all manually in the 
terminal by simply writing `python -m pytest` in the terminal in the root of the project and hit enter.
