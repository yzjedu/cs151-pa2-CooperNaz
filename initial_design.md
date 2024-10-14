# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully

1. Output the purpose of the program and the rules of the game
2. Set the sentinel to 'no'
3. Set losses to 0
4. Prompt the user to choose between starting the game with 10 and 100 sticks and set the number of total sticks accordingly
5. While the user says 'yes' to playing again:
   1. While the amount of total sticks is greater than zero:
      1. If the amount of sticks is greater than 0:
         1. Prompt player 1 to input the number of sticks they want to take
         2. While player 1's choice is not 1, 2, or 3:
            1. Output that the value is invalid
            2. Prompt the user to try again
         3. Subtract the number of sticks taken from the number of total sticks
         4. Output the number of sticks player 1 chose
         5. Output the number of sticks left
      2. If the amount of sticks is greater than 0:
         1. Prompt player 2 to input the number of sticks they want to take
         2. While player 2's choice is not 1, 2, or 3:
            1. Output that the value is invalid
            2. Prompt the user to try again
         3. Subtract the number of sticks taken from the number of total sticks
         4. Output how many sticks player 2 chose
         5. Output the number of sticks left
      3. If the amount of sticks is greater than 0:
         1. For player 3, the computer, generate a random number from 1 to 3 and assign that to the choice
         2. Subtract the number of sticks taken from the number of total sticks
         3. Output how many sticks player 3 chose
         4. Output the number of sticks left
   2. Assign the loss to whoever takes the last stick
   3. Output whether player 1, 2, or 3 lost
   4. Prompt the user to input whether they want to play again or not
6. Output the number of losses for each player
7. Output 'thank you for playing'