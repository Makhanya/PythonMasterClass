import pyfiglet
from termcolor import colored


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "blue"
    ascii_art = pyfiglet.figlet_format(msg)
    color_ascii = colored(ascii_art, color)
    print(color_ascii)


msg = input("What would you like to print? ")
color = input("What colour? ")
(print_art(msg, color))
