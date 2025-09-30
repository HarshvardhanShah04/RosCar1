#!/usr/bin/env python3

import sys
import tty
import termios

def get_char_raw():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch


def main():
    print("Press any key (press q to quit):")
    get_char_raw()

    while True:
        key = get_char_raw()
        print(f"Your pressed the key: {repr(key)}")

        if key == 'q':
            print("Exiting the program...")
            break


if __name__ == '__main__':
    main()