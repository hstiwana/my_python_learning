#!/usr/bin/env python3
# this is created to count number of words in given file
import sys
import timeit

def word_count():
    if len(sys.argv) >= 2:
        in_file = sys.argv[1]
    else:
        print('Fatal: You forgot to include the file name on the command line.')
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

    # Set up an empty dictionary to start a standard design pattern loop
    words_dic = {}
    
    # This loop adds each word to the dictionary and updates its count. Change 
    # all words to lower case so Horse and horse are seen as the same word.
    for line in fhand:
        # remove : e.g. /etc/passwd file has it
        line = line.replace(':', ' ')
        for word in line.lower().split():
                # strip out the stuff we ignore
                word = word.strip("'?,.;!-/\"")
                if word not in words_dic:
                    # add word to words with 0 count
                    words_dic[word] = 0
                # add 1 to the count
                words_dic[word] = words_dic[word] + 1

    # don't forget to close the file handle, good practice
    fhand.close()
    #### Method 1 #####
    # Sorts the dictionary words into a list and then print them out 
    # with reverse mode set to false
    for my_word,my_counter in sorted(words_dic.items(), key=lambda some_lambda_fun_name_p:some_lambda_fun_name_p[1], reverse=False):
        print(my_counter,my_word)
    print("_"*30)
    #### Method 2 #####
    #### NOTE: we are missing reversed sort in this one
    # Sorts the dictionary words into a list and then print them out
    # print("List of words in the file with number of times each appears.")
    # word_list = sorted(words_dic)
    # for word in word_list:
    #     print(words_dic[word], word)

if __name__ == '__main__':
# Lets see how much time it is taking to calculate
# NOTE: time taken to input is also counted as function is waiting for user input    
    print('Total time taken:', timeit.timeit('word_count()', setup='from __main__ import word_count',number=1))

