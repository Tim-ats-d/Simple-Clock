
import datetime
import math


class TextAttributes:
    """A context manager to manage curses text attributs."""

    def __init__(self,
                 stdscr,
                 *attributes):
        self.win = stdscr
        self.attributes = attributes

    def __enter__(self):
        """Activates one by one the attributes contained in
        self.attributes.
        """
        for attr in self.attributes:
            self.win.attron(attr)

    def __exit__(self, type, value, traceback):
        """Disable one by one the attributes contained in
        self.attributes.
        """
        for attr in self.attributes:
            self.win.attroff(attr)


def center(string: str, x: int) -> int:
    """Returns centering calculations depending on the length of string."""
    return int((x//2) - (len(string)//2) - len(string)%2) 


def day_flow() -> str:
    """Returns a string containing the percentage of the day elapsed."""
    nb_seconds_per_day = 86400
    current_time = datetime.datetime.now()

    elapsed_seconds = datetime.timedelta(hours=current_time.hour,
                                         minutes=current_time.minute,
                                         seconds=current_time.second).total_seconds()
    percentage_day_elapsed = elapsed_seconds/nb_seconds_per_day*100

    return str(math.floor(percentage_day_elapsed))
