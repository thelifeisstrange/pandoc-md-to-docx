#!/usr/bin/env python3
import os
import sys

# Auto-activate the virtual environment so you don't have to remember to run 'source'
venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venv', 'bin', 'python')
if os.path.exists(venv_python) and sys.executable != venv_python:
    os.execl(venv_python, venv_python, *sys.argv)

import pypandoc
import argparse
import glob
import curses

def convert_md_to_docx(input_file, output_file=None):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return
        
    if output_file is None:
        # Default output file name: replace .md with .docx
        base_name, _ = os.path.splitext(input_file)
        output_file = f"{base_name}.docx"
        
    if os.path.exists(output_file):
        print(f"Warning: The file '{output_file}' already exists.")
        while True:
            choice = input("Do you want to (r)eplace it, (c)reate new, or (s)kip? [r/c/s]: ").strip().lower()
            if choice == 'r':
                break
            elif choice == 'c':
                counter = 1
                base_name, ext = os.path.splitext(output_file)
                while os.path.exists(f"{base_name} ({counter}){ext}"):
                    counter += 1
                output_file = f"{base_name} ({counter}){ext}"
                break
            elif choice == 's':
                print(f"Skipped '{input_file}'.")
                return
            else:
                print("Invalid choice. Please enter 'r', 'c', or 's'.")
                
    print(f"Converting '{input_file}' to '{output_file}'...")
    
    try:
        # pypandoc.convert_file converts the file and saves it
        pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
        print(f"Conversion successful! Output saved to: {output_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")
        print("Note: If you haven't installed 'pypandoc_binary', you might need to install 'pandoc' on your system.")
        return

def select_file_interactive(files):
    def menu(stdscr):
        try:
            curses.use_default_colors()
        except curses.error:
            pass
        
        try:
            curses.curs_set(0) # Hide cursor
        except curses.error:
            pass
        current_row = 0
        selected = set()
        options = list(files) + ["[ Convert Selected ]", "[ Cancel ]"]
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Select Markdown files to convert (SPACE to select, ENTER to confirm, ESC to cancel):\n\n")
            
            for idx, item in enumerate(options):
                if idx < len(files):
                    is_selected = "x" if idx in selected else " "
                    display_text = f"[{is_selected}] {item}"
                else:
                    display_text = item
                
                if idx == current_row:
                    stdscr.addstr(idx + 2, 0, f" > {display_text}", curses.A_REVERSE)
                else:
                    stdscr.addstr(idx + 2, 0, f"   {display_text}")
            
            stdscr.refresh()
            key = stdscr.getch()
            
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < len(options) - 1:
                current_row += 1
            elif key == ord(' '):
                if current_row < len(files):
                    if current_row in selected:
                        selected.remove(current_row)
                    else:
                        selected.add(current_row)
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row == len(options) - 1: # Cancel
                    return []
                elif current_row == len(options) - 2: # Convert Selected
                    if not selected:
                        return []
                    return [files[i] for i in sorted(selected)]
                else: # Enter on a file
                    if not selected:
                        return [files[current_row]]
                    return [files[i] for i in sorted(selected)]
            elif key == 27:  # ESC key
                return []
    return curses.wrapper(menu)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown files to Word Documents (.docx)")
    parser.add_argument("input", nargs="*", help="Paths to the input Markdown (.md) files. Optional.", default=[])
    parser.add_argument("-o", "--output", help="Path to the output Word Document (.docx). Only applies if a single input file is provided.", default=None)
    
    args = parser.parse_args()
    
    # If specific files are provided, convert them
    if args.input:
        if len(args.input) == 1:
            convert_md_to_docx(args.input[0], args.output)
        else:
            if args.output:
                print("Warning: --output is ignored when multiple input files are provided.")
            for f in args.input:
                convert_md_to_docx(f)
    else:
        # If no file is provided, show the interactive menu
        md_files = glob.glob("*.md")
        if not md_files:
            print("No Markdown (.md) files found in the current directory.")
        else:
            selected_files = select_file_interactive(md_files)
            if selected_files:
                for f in selected_files:
                    convert_md_to_docx(f)
            else:
                print("Conversion cancelled.")
