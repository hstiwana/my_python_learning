#!/usr/bin/env python
# This script is to emulate classic game of "rock" "paper" "scissors"

# we are going to use functions from 2 classes "sys" and "random"
import sys, random

def game_users(users_dict):
    number_of_tries_for_input = 5

    #run a loop to get valid input from user
    # if all tries are used, exit
    for i in range(1,number_of_tries_for_input + 1):
        try:
            num_of_players = int(input('Number of players : '))
            # we need minimum 1 player for this game to play with computer
            # if user entered 0, run this code ... also run this code if user
            # entered a value larger than 6
            if num_of_players < 1 or num_of_players > 6:
                print('Please input a valid number for player count (Max 6): ')
                print(f'You tried {i} times')
                # Validate and exit if all tries are done
                if i == number_of_tries_for_input:
                    print(f'\nMax {number_of_tries_for_input} tries done!')
                    sys.exit()
                continue

            # if user has provided valid input, get out of loop
            else:
                break

        # validate and handle invalid input
        except ValueError:
            print(f'Please enter number only, you tried {i} times')
            # Validate and exit if all tries are done
            if i == number_of_tries_for_input:
                print(f'\nMax {number_of_tries_for_input} tries done!')
                sys.exit()
            # if not all tries done, send user back to looping
            continue
        # if ctrl+c is called, exit out without error
        except KeyboardInterrupt:
            sys.exit()
        break

    try:
        # get user input or stay in the loop
#        while True:
            # if entered value is not a digit and it is positive integer
            # we need minimum 1 player for this game to play with computer
#            if not num_of_players.isdigit() or int(num_of_players) < 1 or int(num_of_players) > 6:
#            if num_of_players < 1 or num_of_players > 6:
#                print('Please input a valid number for player count (Max 6): ')
#                num_of_players = input('Number of players: ')
            # if user has provided valid input, get out of loop
#            else:
#                break

        # create an empty Dictionary and use later to append values in it.
        users_dict={}
        #    users = game_users() # call function to get user count and validate input
        print(f'{num_of_players} Players')
        for user_n in range(1,int(num_of_players)+1):# since range starts from 0, we are asking it to start from 1 and moving users by 1
            user_num = ( user_n - 1 )
            users_dict[user_num] = input(f'Please input name for user {user_n} : ')
            # debug code: to see a particular dictionary index value
            # print(f'User {user_num} = {users_dict[user_num]}')
        # debug code: to see dictionary contents
        #print(f'Printing entire user list {users_dict}')
    except KeyboardInterrupt:
        sys.exit()
    return users_dict

def rps_game():
    try:
        # Some variables to keep the count
        wins = 0
        ties = 0
        losses = 0
        # calling function within next function
        # print('call game_users(users_dict) function within rps_game() function')
        users_dict=""
        users_dict_list=game_users(users_dict)
        #print(game_users(users_dict))
        print(f'Users from previous function: {users_dict_list}')
        # Create a list to use as computer move
        computer_list = ['r','p','s']
        # Assign a random move to computer from computer_list
        computerMove = computer_list[random.randint(0, 2)]
        # Main infinite game loop
        while True:
            print(f'Welcome to Rock Paper Scissors Game!!!')
            #User input loop, keep looping unless user selects a valid option
            while True:
                playerMove=input('Please select an option: (r)ock, (p)aper, (s)scissor, (q)uit : ')
                if playerMove == computerMove:
                    print('It is a Tie!')
                    # Increment count
                    ties += 1
                elif playerMove == 'r' and computerMove == 'p':
                    print(f'You loose, your choice was {playerMove} and Computer choose {computerMove} , Paper covers Rock!!')
                    losses += 1# Increment count
                elif playerMove == 'r' and computerMove == 's':
                    print(f'You win your choice was {playerMove} and Computer choose {computerMove} ,Rock smashes Scissor')
                    wins += 1# Increment count
                elif playerMove == 's' and computerMove == 'p':
                    print(f'You win your choice was {playerMove} and Computer choose {computerMove} ,Scissor cuts paper!')
                    wins += 1# Increment count
                elif playerMove == 's' and computerMove == 'r':
                    print(f'You loose, your choice was {playerMove} and Computer choose {computerMove} , Rock smashes scissor')
                    losses += 1# Increment count
                elif playerMove == 'p' and computerMove == 'r' :
                    print(f'You win, your choice was {playerMove} and Computer choose {computerMove} ,Paper covers rock!!')
                    wins += 1# Increment count
                elif playerMove == 'p' and computerMove == 's':
                    print(f'You loose, your choice was {playerMove} and Computer choose {computerMove} , scissor cuts paper')
                    losses += 1# Increment count
                elif playerMove == 'q':
                    # Print final score if user decided to quit using option q
                    print('\nThanks for playing!!!\n')
                    total_games_played = wins + losses + ties
                    print(f'Total Games played : {total_games_played}, Your Final Score : Wins: {wins}, Loose: {losses}, Tie: {ties}')
                    if wins > losses:
                        print('\nOverall you BEAT the Computer!!!...Good JOB!!!\n')
                    elif losses > wins:
                        print('\nComputer got better of you!..Better luck next time!!!\n')
                    else:
                        print('\nYou and Computer were at par...!!\n')
                    sys.exit()
                else:
                    print('Please choose a valid option ')
                # Again select a random move for computer.
                computerMove = computer_list[random.randint(0, 2)]
    except KeyboardInterrupt:
        # Print final score if user decided to quit using option q
        print('\nThanks for playing!!!\n')
        sys.exit()

# finally call the functions
if __name__ == '__main__':
        rps_game()
