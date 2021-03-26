
import curses
import curses.textpad
import datetime
import time
from typing import Dict, NoReturn

from utils import center, day_flow, TextAttributes


ConsoleEffect = NoReturn

infos: Dict[str, str] = {
    "hour_format": "%H:%M:%S",
    "date_format": "%d/%m/%y",
    "day_percent": "{} % of the day elapsed.",
    "statusbar": "The time was given to you by Tim."
}


def main(stdscr) -> ConsoleEffect:
    """curses rendering."""
    curses.curs_set(False)
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

    while 1:
        rows, cols = stdscr.getmaxyx()

        (x_hour,
         x_date,
         x_day_percent,
         x_statusbar) = (center(info, cols)
                             for info in infos.values())
        middle_y = rows//2 - rows//2//2

        stdscr.clear()

        stdscr.box()
        curses.textpad.rectangle(stdscr,
                       middle_y - 2,
                       x_hour - len(infos["statusbar"])//2 + 2,
                       middle_y + 4,
                       x_hour + len(infos["statusbar"])//2 + 3)

        with TextAttributes(stdscr, curses.color_pair(1)):
            stdscr.addstr(middle_y,
                          x_hour,
                          time.strftime(infos["hour_format"]))
            stdscr.addstr(middle_y + 2,
                          x_date,
                          time.strftime(infos["date_format"]))          
            stdscr.addstr(middle_y + 6,
                          x_day_percent,
                          infos["day_percent"].format(day_flow()))

        with TextAttributes(stdscr, curses.color_pair(2)):
            stdscr.addstr(middle_y + 8,
                          x_statusbar,
                          time.strftime(infos["statusbar"]))

        stdscr.refresh()
        time.sleep(1)


if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        ...
