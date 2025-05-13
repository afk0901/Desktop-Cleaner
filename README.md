# 🧹 Desktop Organizer – Python Automation Tool

Tired of your cluttered Desktop?

**Desktop Organizer** is a simple yet powerful Python automation tool built for Windows that brings instant order to your chaos. It scans your Desktop and automatically moves files into folders based on file extensions — no clicks, no dragging, no nonsense.

Whether it's scattered PDFs, Word docs, Excel sheets, or plain text files, this script puts everything in its place. Clean workspace, clear mind.

## ✅ Current Features

- Automatically sorts:
  - `.pdf` → `PDF Documents`
  - `.docx`, `.doc` → `Word Documents`
  - `.xlsx`, `.xls`, `.odt` → `Excel Documents`
  - `.txt` → `Text Documents`
- Resolves correct Desktop path (supports OneDrive and standard setups)

## How to run the tool

Download the installer from this repository or clone the repo and follow the instructions below.

The main entry file is desktop_organizer.py. Run it in your IDE or run this command inside the
root directory of the project: `python desktop_organizer.py`. This command should start the
tool.

## 🧪 Tests

This project includes automated tests to verify file movement behavior and handle edge cases safely.

The project uses Pytest for all it's tests. Run it in your IDE or run Pytest manually in the 
terminal by simply write `python pytest` in the terminal in the root of the project and hit enter and it should run all the tests. 
