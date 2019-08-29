#!/usr/bin/env python3

r"""LoveU

Usage:
    loveu.py NAME
    loveu.py (-h | --help)
    loveu.py (-v | --version)

Arguments:
    NAME    Lover's name

Options:
    -h, --help
    -v, --version
"""

import time
from docopt import docopt


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    #print("[DEBUG] args =", args)

    lover_name = args["NAME"]
    hearts = []

    for i in range(101):
        i = 1.8 - i*0.01
        hearts.append(
            '\n'.join(
                [
                    ''.join([(
                            ('.Love' + lover_name)[(x-y) \
                            % (5 + len(lover_name))] \
                            if ((x*0.05*i)**2 + (y*0.1*i)**2 - 1)**3 \
                            - (x*0.05*i)**2 * (y*0.1*i)**3 <= 0 \
                            else ' '
                        ) for x in range(-30, 30)
                    ]) for y in range(15, -15, -1)
                ]
            )
        )

    try:
        print("\033[31m")
        while True:
            for heart in hearts:
                print("\033[H\x1b[2J")
                print(heart)
                time.sleep(0.01)

            for heart in hearts[::-1]:
                print("\033[H\x1b[2J")
                print(heart)
                time.sleep(0.01)
    except KeyboardInterrupt:
        pass
