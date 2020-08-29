import datetime
import curses
import time
import os



ROWS, COLS = os.get_terminal_size()

def hour() -> str:
    """
        Returns a string containing current hour, minute and second.
    """

    return time.strftime("%H:%M:%S")



def date() -> str:
    """
        Returns a string containing current day, month, year.
    """

    return time.strftime("%d/%m/%y")



def day_flow() -> str:
    """
        Returns a string containing the percentage of the day elapsed.
    """

    current_hour = datetime.datetime.now()
    percentage_day_elapsed = round(
                                        datetime.timedelta(
                                                            hours=current_hour.hour,
                                                            minutes=current_hour.minute,
                                                            seconds=current_hour.second
                                                          ).total_seconds()/86400*100,
                                        2
                                      )

    return str(percentage_day_elapsed)



def grid(width: int, length: int) -> str:
    """
        Prints a grid in ASCII character with a width and length.
    """

    starting_line = f"╔{length*'═'}╗"
    end_line = f"╚{length*'═'}╝"

    return "\n".join((starting_line, "\n".join((f"║{' '*length}║" for line in range(width))), end_line))



def screen(stdscr):
    """
        curses rendering.
    """

    stdscr.clear()
    curses.curs_set(0)
    curses.resizeterm(12, 41)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

    statusbar = "The time was given to you by Tim." .center(COLS, " ")

    stdscr.addstr(0, 0, grid(5, 38))
    stdscr.addstr(2, 15, date(), curses.color_pair(1))
    stdscr.addstr(11, 0, statusbar.center(40), curses.color_pair(2))

    while 1:
        stdscr.addstr(4, 15, hour(), curses.color_pair(1))
        stdscr.addstr(8, 0, f"{day_flow()} % of the day elapsed.".center(40), curses.color_pair(1))

        stdscr.refresh()
        time.sleep(1)



if __name__ == "__main__":
    curses.wrapper(screen)

