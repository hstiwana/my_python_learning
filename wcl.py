#!/usr/bin/env python3
# replicate "wc" command from Unix
# - lwc.py *- coding: utf-8 -*-
import sys
def helper():
        print('\nFatal: You forgot to include the file name on the command line.')
        print(f'\nUsage: To see count of all lines:  python {sys.argv[0]} /etc/hosts')
        print(f'''Options: 
                        -w : word count
                        -c : character count
                        -l : line count
                        -t : show time taken''')
        print(f'\nUse -h/-H/-help/--help as argument to see usage/this message\n')
        quit()
def wcl():
    # lets initialize variable with None value
    in_file = None
     # make a tuple of helper function callers
    helper_args = ('-h','-H','--help','-help')

    for helper_arg in helper_args:
        # Call helper function only if argument list contains one of the tuple item
        if sys.argv.__contains__(helper_arg): helper()

    ## Check if we have 2 or more arguments
    if len(sys.argv) >= 2:
            # sys.argv[0] is the script/program name, we start with 1st argument
            for arg in sys.argv[1:]:
                # if argument is starting with "-", we skip it
                if arg.startswith('-'): continue
                # else we can assume it is a filename
                else: in_file = arg    
    # if less than 2 arguments are passed, assume missing filename
    else: helper()
    
    # after checking all attributes, if we don't have in_file set, we call helper function.
    if in_file == None: helper()

    # lets "try" to open file passed as argument and handle few exceptions    
    try: text_file = open(in_file,'r')
    except FileNotFoundError: print(f'"{in_file}" , File not found, please try again! with valid file path'); quit()
    except IsADirectoryError: print(f'"{in_file}" , is a directory, please try again! with valid file path'); quit()
    except PermissionError:print(f'"{in_file}" , you don\'t have permissions to read this file!'); quit()

    # initialize line, word, and char counters to 0
    linect = 0
    wordct = 0     
    charct = 0
    
    for line in text_file:           # step through each line in the text file
        linect = linect + 1
        charct = charct + len(line)
    
        for word in line.split():    # split into a list of words
            wordct = wordct + 1
    # close the file handle
    text_file.close()
    
    # handle arguments
    if sys.argv.__contains__('-l') and sys.argv.__contains__('-w') and sys.argv.__contains__('-c'):
        print(f'\t{linect}\t{wordct}\t{charct}\t{in_file}')
    elif ((sys.argv.__contains__('-l') and sys.argv.__contains__('-w')) or (sys.argv.__contains__('-lw') or sys.argv.__contains__('-wl'))):
        print(f'\t{linect}\t{wordct}\t{in_file}')
    elif ((sys.argv.__contains__('-l') and sys.argv.__contains__('-c')) or (sys.argv.__contains__('-lc') or sys.argv.__contains__('-cl'))):
        print(f'\t{linect}\t{charct}\t{in_file}')
    elif ((sys.argv.__contains__('-w') and sys.argv.__contains__('-c')) or (sys.argv.__contains__('-wc') or sys.argv.__contains__('-cw'))):
        print(f'\t{wordct}\t{charct}\t{in_file}')
    elif sys.argv.__contains__('-l'):
        print(f'\t{linect}\t{in_file}')
    elif sys.argv.__contains__('-w'):
        print(f'\t{wordct}\t{in_file}')
    elif sys.argv.__contains__('-c'):
        print(f'\t{charct}\t{in_file}')
    else:
        print(f'\t{linect}\t{wordct}\t{charct}\t{in_file}')
    if sys.argv.__contains__('-t'): print("-"*40)

if __name__ == '__main__':
    # if "-t" is one of the arguments, Lets see how much time it is taking to calculate
    # NOTE: time taken to input is also counted as function is waiting for user input
    if sys.argv.__contains__('-t'): 
        import timeit
        print('Total time taken:', timeit.timeit('wcl()', setup='from __main__ import wcl',number=1))
    # else call function wcl()
    else: 
        wcl()
