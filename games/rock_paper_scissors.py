#!/usr/bin/env python
# This script is to emulate classic game of "rock" "paper" "scissors"

# we are going to use functions from 2 classes "sys" and "random"
import sys, random

# Some variables to keep the count
wins = 0
ties = 0
losses = 0

# main gain loop
while True:
    print(f'Stats: Wins({wins}) Losses({losses}) ties({ties})')
    while True: #User input loop, keep looping unless user selects a valid option
        playerMove=input('Please select an option: (r)ock, (p)aper, (s)scissor, (q)uit : ')
        # Print final score if user decided to quit using option q
        if playerMove == 'q':
            print()
            print('All right, exiting game ....')
            print()
            print()
            print(f'Your Final Game Scores: Wins({wins}) Losses({losses}) ties({ties})')
            print()
            sys.exit()
        elif playerMove == 'r':
            print('Rock versus... ',end=' ')
            break
        elif playerMove == 'p':
            print('Paper versus... ',end=' ')
            break
        elif playerMove == 's':
            print('Scissor versus... ',end=' ')
            break
        print('Try again, Valid options are: r, p, s or q')
# Lets get a random number from a function "randint"
    randomNumber = random.randint(1,3)
# Assign computerMoves to match with a randomly generated number
    if randomNumber == 1:
        computerMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissor')
# Compare playerMove and ComputerMoves to get results
    if playerMove == computerMove:
        print('It is a Tie!')    
        ties = ties + 1 # Increment count
    elif playerMove == 'r' and computerMove == 's':
        print('Rock breaks Scissor, You Win!')    
        wins = wins + 1 # Increment count
    elif playerMove == 'p' and computerMove == 'r':
        print('Paper covers Rock, You Win!')    
        wins = wins + 1 # Increment count
    elif playerMove == 's' and computerMove == 'p':
        print('Scissor cut Paper, You Win!')
        wins = wins + 1 # Increment count
    elif playerMove == 'r' and computerMove == 'p':
        print('Paper covers Rock, You Loss!')
        losses = losses + 1 # Increment count
    elif playerMove == 'p' and computerMove == 's':
        print('Scissor cut Paper, You Loss!')
        losses = losses + 1 # Increment count
    elif playerMove == 's' and computerMove == 'r':
        print('Rock breaks Scissor, You Loss!')
        losses = losses + 1 # Increment count
