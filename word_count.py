#!/usr/bin/env python3
# this is created to count number of words in given file

## uncomment it to test the commented out "Method 2" given below 
# import pprint
import sys
import timeit

def word_count():
    if len(sys.argv) >= 2:
        in_file = sys.argv[1]
    else:
        print('Fatal: You forgot to include the directory name on the command line.')
        print(f'Usage:  python {sys.argv[0]} /etc/hosts')
        quit()
    try:
        # lets "try" to open file passed as argument and handle few exceptions
        fhand = open(in_file,'r')
    except FileNotFoundError:
        print(f'"{in_file}" , File not found, please try again! with valid file path')
        quit()
    except IsADirectoryError:
        print(f'"{in_file}" , is a directory, please try again! with valid file path')
        quit()
    except PermissionError:
        print(f'"{in_file}" , you don\'t have permissions to read this file!')
        quit()

    # Read full file into full_text variable
    full_text = fhand.read()

    # don't forget to close the file handle, good practice
    fhand.close()

    # Lets remove all unwanted characters from full_text (str) variable
    # newline and : e.g. /etc/passwd file
    for char in '\n:':
        word_lines = full_text.replace(char,' ')

    # change case to lower to get exact count
    # split text to a get a list out of it
    word_lines = word_lines.lower().split()

    # get only unique values by making a set
    # This will reduce run time as loop will run only N number of times
    # where N will be unique value only (as compared to full fill)
    my_set = set(word_lines)

    # create an empty counter dict a.k.a. initialize it 
    counter={}
    # lets read lines from the file handle we created
    # for word in word_lines:
    #        count[word] = count.get(word,0) + 1
    for unique_val in my_set:
        # use count function of list to give number of times a word is used
        # store it in dictionary "counter" for sorting at later stage
        counter[unique_val] = word_lines.count(unique_val)

    ######## Method 1 sort ##########
    # print count and value from dictionary and 
    # sort it using sorted function with key as "lambda" function named "some_lambda_fun_name_p" and reverse=False
    # Following line is taking value (which is a number) as list, that's why we are using [1] in it.
    #       key=lambda some_lambda_fun_name_p:some_lambda_fun_name_p[1]
    # sorting works well with numbers v/s text, making [0] will produce random results.
    for key,value in sorted(counter.items(), key=lambda some_lambda_fun_name_p:some_lambda_fun_name_p[1], reverse=False):
        print(value,key)
    print("_"*30)
    ####### Method 2 to sort #########
    #### it has limitations, outout is shown as dictionary for each word
    #### shows incorrect count too

    ## Create a new empty list to sort
    # word_freq = []
    # for key, value in count.items():
    #     # Assign Value first and key second to make it easy to sort
    #     # use a dict to assign 
    #     word_freq.append({value, key})
    ## reverse sort the list
    # word_freq.sort(reverse=True)
    ## Pretty print to show output on next line, uncomment import statement on top
    # pprint.pprint(word_freq)

if __name__ == '__main__':
# Lets see how much time it is taking to calculate
# NOTE: time taken to input is also counted as function is waiting for user input    
    print('Total time taken:', timeit.timeit('word_count()', setup='from __main__ import word_count',number=1))