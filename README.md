# Markdown to Docx Converter

A Python-based command-line tool that provides a seamless, interactive way to convert Markdown (`.md`) files into Microsoft Word (`.docx`) documents. This is especially useful for quickly exporting documentation, notes, or code READMEs into a widely distributable Word format, bypassing any formatting issues when copying directly from text editors like VS Code.

## Features

- **Interactive UI**: Features a clean terminal UI (using `curses`) that lets you scroll and select files with your keyboard.
- **Batch Processing**: Select multiple Markdown files at once (using the `SPACE` bar) to convert them all in a single run.
- **Safe Overwriting**: Automatically checks if a `.docx` file already exists and prompts you to either replace it, create a new file (e.g., `filename (1).docx`), or skip the file entirely.
- **Command-Line Arguments**: Supports direct conversion via CLI arguments without launching the interactive menu.
- **Isolated Environment**: Automatically activates its own Python virtual environment (`venv`) to keep dependencies self-contained.

## Requirements

- **Python 3.x**
- **Pandoc**: Ensure Pandoc is installed on your system. If not, the script will utilize `pypandoc_binary` if installed.

## Installation

1. Clone or download this repository.
2. Ensure you have the required Python dependencies installed (a virtual environment is recommended).
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pypandoc pypandoc_binary
   ```

## Usage

You can run the script with or without arguments.

### Interactive Mode
Run the script without any arguments to open the interactive selection menu:
```bash
./md_to_docx.py
```
- **UP / DOWN**: Navigate the list of files.
- **SPACE**: Select/deselect files for batch conversion.
- **ENTER**: Confirm and convert selected files.
- **ESC**: Cancel and exit.

### Command-Line Mode
Convert a single file directly:
```bash
./md_to_docx.py input.md
```

Convert multiple files:
```bash
./md_to_docx.py file1.md file2.md file3.md
```

Specify a custom output file name (only works when converting a single file):
```bash
./md_to_docx.py input.md -o custom_name.docx
```
