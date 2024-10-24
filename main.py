# Programmers:  Cooper Nazar
# Course:  CS151, Professor Yalew
# Due Date: October 23, 2024
# Programming Assignment:  PA 02
# Problem Statement: Create a three-player game of the Game of Sticks
# Data In: Number of sticks chosen, whether to play again or not
# Data Out: Losses
# Credits:

import random

# Output purpose of the program
print('\nHello! Welcome to the Game of Sticks!')
print('This game includes three players, one of which is part of the program!')

# Output the rules
print('\nRULES:')
print('\t1. The game starts with a set amount of sticks: 10 or 100')
print('\t2. Three players take turns choosing how many sticks to take')
print('\t3. On your turn, you must take either 1, 2, or 3 sticks')
print('\t4. The player who takes the last stick loses')

# Set the sentinel to 'no'
SENTINEL = 'no'

# Create a variable for the play again decision
replay = 'yes'

# Set all players' losses to 0
player1_loss = 0
player2_loss = 0
player3_loss = 0

# Start the loop that will run until the player decides to stop
while replay != 'no' and replay == 'yes':

      # Ask the user to choose which game mode they will play
      print('\nGAME MODES:')
      print('\t1. 10 sticks')
      print('\t2. 100 sticks')
      game_mode = int(input('\nWhich game mode would you like to play? '))

      # Make sure that the user chooses game mode 1 or 2
      while game_mode != 1 and game_mode != 2:
            print('\nInvalid input. Please try again.')
            game_mode = int(input('\nWhich game mode would you like to play? '))

      # Set the number of total sticks based on the game mode
      if game_mode == 1:
            total_sticks = 10
      else:
            total_sticks = 100
      sticks = total_sticks

      # Set up each player's turn to run when the number of total sticks is greater than zero
      # For each, subtract the player's choice from the number of sticks and output the remaining sticks
      # When a player is left with one stick, they lose because they can only take the last stick
      while sticks > 0:
            if sticks > 1:
                  player1_choice = int(input('\nPlayer 1, how many sticks would you like to take? '))
                  while player1_choice != 1 and player1_choice != 2 and player1_choice != 3:
                        print('\nInvalid input. Please try again.')
                        player1_choice = int(input('\nPlayer 1, how many sticks would you like to take? '))
                  sticks -= player1_choice
                  print(f'\nThere are {sticks} sticks left.')
            elif sticks == 1 or sticks == 0:
                  print('\nPlayer 1 loses! Thanks for playing!')
                  sticks = -10 # Random value that can't be achieved through user input
                  player1_loss += 1
            else:
                  print('')

            if sticks > 1:
                  player2_choice = int(input('\nPlayer 2, how many sticks would you like to take? '))
                  while player2_choice != 1 and player2_choice != 2 and player2_choice != 3:
                        print('\nInvalid input. Please try again.')
                        player2_choice = int(input('\nPlayer 2, how many sticks would you like to take? '))
                  sticks -= player2_choice
                  print(f'\nThere are {sticks} sticks left.')
            elif sticks == 1 or sticks == 0:
                  print('\nPlayer 2 loses! Thanks for playing!')
                  sticks = -10
                  player2_loss += 1
            else:
                  print('')

            if sticks > 1:
                  player3_choice = random.randint(1,3)
                  sticks -= player3_choice
                  print(f'\nPlayer 3 chose {player3_choice} sticks.')
                  print(f'\nThere are {sticks} sticks left.')
            elif sticks == 1 or sticks == 0:
                  print('\nPlayer 3 loses! Thanks for playing!')
                  sticks = -10
                  player3_loss += 1
            else:
                  print('')



      # Output the number of losses for each player

      print('\nRESULTS:')
      print(f'\tPlayer 1 lost {player1_loss} times.')
      print(f'\tPlayer 2 lost {player2_loss} times.')
      print(f'\tPlayer 3 lost {player3_loss} times.')

      # Prompt the user to input if they want to play again or not
      replay = input('\nWould you like to play again? ')
      replay = replay.lower().strip()
      if replay != 'yes' and replay != 'no':
            print('\nInvalid input. Please input yes or no.')
            replay = input('\nWould you like to play again? ')
            replay = replay.lower().strip()

# Output the number of losses for each player
print('\nRESULTS:')
print(f'\tPlayer 1 lost {player1_loss} times.')
print(f'\tPlayer 2 lost {player2_loss} times.')
print(f'\tPlayer 3 lost {player3_loss} times.')

# Print a thank-you message
print('\nThank you for playing!')
print('\nClosing the game.\n')