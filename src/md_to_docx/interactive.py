from __future__ import annotations

import curses
from typing import Sequence


def select_files_interactive(files: Sequence[str]) -> list[str]:
    if not files:
        return []

    def menu(stdscr):
        try:
            curses.use_default_colors()
        except curses.error:
            pass

        try:
            curses.curs_set(0)
        except curses.error:
            pass

        current_row = 0
        selected: set[int] = set()
        options = list(files) + ["[ Convert Selected ]", "[ Cancel ]"]

        while True:
            stdscr.clear()
            stdscr.addstr(
                0,
                0,
                "Select Markdown files to convert (SPACE to select, ENTER to confirm, ESC to cancel):\n\n",
            )

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
            elif key == ord(" "):
                if current_row < len(files):
                    if current_row in selected:
                        selected.remove(current_row)
                    else:
                        selected.add(current_row)
            elif key == curses.KEY_ENTER or key in (10, 13):
                if current_row == len(options) - 1:
                    return []
                if current_row == len(options) - 2:
                    if not selected:
                        return []
                    return [files[i] for i in sorted(selected)]
                if not selected:
                    return [files[current_row]]
                return [files[i] for i in sorted(selected)]
            elif key == 27:
                return []

    return curses.wrapper(menu)
