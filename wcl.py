#!/usr/bin/env python3
# replicate "wc" command from Unix
# - lwc.py *- coding: utf-8 -*-
import sys
def helper():
        print('Fatal: You forgot to include the file name on the command line.')
        print(f'Usage: To see count of all lines:  python {sys.argv[0]} /etc/hosts')
        print(f'\nUse -h/-H/-help/--help as argument to see usage/this message\n')
        quit()
def wcl():
     # make a tuple of helper function callers
    helper_args = ('-h','-H','--help','-help')
    for helper_arg in helper_args:
        # Call helper function only if argument list contains one of the tuple item
        if sys.argv.__contains__(helper_arg):
            helper()
    # Check if we have 2 or more arguments
    if len(sys.argv) >= 2:
        in_file = sys.argv[1]
    else:
        # if argument list is not 2 or more, call helper function
        helper()
    try:
        # lets "try" to open file passed as argument and handle few exceptions
        text_file = open(in_file,'r')
    except FileNotFoundError:
        print(f'"{in_file}" , File not found, please try again! with valid file path')
        quit()
    except IsADirectoryError:
        print(f'"{in_file}" , is a directory, please try again! with valid file path')
        quit()
    except PermissionError:
        print(f'"{in_file}" , you don\'t have permissions to read this file!')
        quit()

    

    # initialize line, word, and char counters to 0
    linect = 0
    wordct = 0     
    charct = 0
    
    for line in text_file:           # step through each line in the text file
        linect = linect + 1
        charct = charct + len(line)
    
        for word in line.split():    # split into a list of words
            wordct = wordct + 1
    
    text_file.close() 
                   
    print(f'\t{linect}\t{wordct}\t{charct}\t{in_file}')

if __name__ == '__main__':
    # Lets see how much time it is taking to calculate
    # NOTE: time taken to input is also counted as function is waiting for user input
    if sys.argv.__contains__('timeit'):
        import timeit
        print('Total time taken:', timeit.timeit('wcl()', setup='from __main__ import wcl',number=1))
    else:
        wcl()
