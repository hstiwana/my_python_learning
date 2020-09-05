#!/usr/bin/env python
# This program is a going to print zig zag stars on screen
# we are hadling keyboard interrupt to stop it
# without interrupt, it is an infinite loop

# we are using time and sys functions
# time for sleep and sys for exit
# without time.sleep, program runs too fast and it is hard to see it scrolling

import time, sys
indent = 0 # Denotes how many spaces to indent
indentIncreaseing = True # Whether the indentation is increaseing or decreasing.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')# print by multiplecation with spaces, replace newline end with empty string.
        print('********')
        time.sleep(0.1) # Pause I/O for 1/10 of a second.

        if indentIncreaseing:
            # Increase the number of spaces.
            indent = indent + 1
            if indent == 20:
                # Change direction
                indentIncreaseing = False
        else:
            # Decrease the number of spaces.
            indent = indent - 1
            if indent == 0:
                # Change direction.
                indentIncreaseing = True
except KeyboardInterrupt: #keyboard interrupt will send program to sys.exit()
    sys.exit()

