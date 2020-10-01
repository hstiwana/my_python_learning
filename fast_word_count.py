#!/usr/bin/env python3
# this is created to count number of words in given file
import sys
import timeit

def word_count():
    if len(sys.argv) >= 2:
        in_file = sys.argv[1]
    else:
        print('Fatal: You forgot to include the file name on the command line.')
        print(f'Usage: To see count of all lines:  python {sys.argv[0]} /etc/hosts')        
        print(f'Usage: To limit line count to top few e.g. top 5 : python {sys.argv[0]} /etc/hosts 5')
        print(f'Usage: To limit line count to top few e.g. top 5 in reverse order : python {sys.argv[0]} /etc/hosts 5 reverse')
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
    
    # if we have 3rd argument, and it is a digit, lets use this to show number of lines
    # similar to "tail" command in Unix.
    if len(sys.argv) >= 3:
        if (sys.argv[2]).isdigit():
            print_n_lines = int(sys.argv[2])
        else:
            # if argument is not a digit, we show full file
            print_n_lines=-1
    else:
        # if argument is not a digit, we show full file
        print_n_lines=-1
    
    # handle sorting with another argument
    # if argument list contains "reverse"
    # show reversed output (with highest number at the top/begining)
    # otherwise show a normal sorted output (with highest number at the bottom/end)
    if sys.argv.__contains__("reverse"):
        reverse=True
        res = dict(sorted(words_dic.items(), key=lambda some_lambda_fun_name_p:some_lambda_fun_name_p[1], reverse=reverse)[:print_n_lines])
    else:
        reverse=False
        res = dict(sorted(words_dic.items(), key=lambda some_lambda_fun_name_p:some_lambda_fun_name_p[1], reverse=reverse)[-print_n_lines:])
    #res = dict(sorted(words_dic.items(), key=lambda some_lambda_fun_name_p:some_lambda_fun_name_p[1], reverse=reverse)[-print_n_lines:])
    for my_word,my_counter in res.items():
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

