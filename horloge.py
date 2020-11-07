#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import curses
import datetime
import os
import time


ROWS, COLS = os.get_terminal_size()

def center(string: str) -> int:
    """Returns centering calculations depending on the length of string."""
    return int((ROWS//2) - (len(string)//2) - len(string)%2)


def hour() -> str:
    """Returns a string containing current hour, minute and second."""
    return time.strftime("%H:%M:%S")


def date() -> str:
    """Returns a string containing current day, month, year."""
    return time.strftime("%d/%m/%y")


def day_flow() -> str:
    """Returns a string containing the percentage of the day elapsed."""
    current_hour = datetime.datetime.now()
    percentage_day_elapsed = round(
                                 datetime.timedelta(
                                     hours=current_hour.hour,
                                     minutes=current_hour.minute,
                                     seconds=current_hour.second).total_seconds()/86400*100,
                                 2)

    return str(percentage_day_elapsed)


def grid(length: int, width: int, centersize: int) -> str:
    """Returns a grid in ASCII character with length and width centersize centered to centersize."""
    starting_line = f"╔{length*'═'}╗".center(centersize)
    end_line = f"╚{length*'═'}╝".center(centersize)

    return "".join(
               (starting_line,
                "".join((f"║{' '*length}║".center(centersize) for line in range(width))),
                end_line)
           )


def main(stdscr):
    """curses rendering."""
    stdscr.clear()
    curses.curs_set(0)
    curses.resizeterm(COLS, ROWS)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    statusbar = "The time was given to you by Tim."

    start_x_time = center(hour())
    start_x_statusbar = center(statusbar)

    stdscr.addstr(7, 0, grid(40, 5, ROWS))
    stdscr.addstr(18, start_x_statusbar, statusbar, curses.color_pair(2))

    key = 0

    while key != ord("q"):
        stdscr.addstr(9, start_x_time, date(), curses.color_pair(1))
        stdscr.addstr(11, start_x_time, hour(), curses.color_pair(1))
        stdscr.addstr(15, 0, f"{day_flow()} % of the day elapsed.".center(ROWS), curses.color_pair(1))

        stdscr.refresh()
        time.sleep(1)
        key = stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
