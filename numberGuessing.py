# Date: 12/19/2024 | STATUS: COMPLETE

# Project: 
#     Program thinks of a random number 1 to 100.
#     User will be prompted to guess a number 1 to 100.
#     Program will tell the user if they're lower or higher than the correct number.else
#     Will congratulate the user if they suceed
#     If user gives up, they can input '0' to quit. Program will tell the user what the answer was.

# What I learned:
# - The random method and its use
# - Variables and the need to not initialize them to a data type
# - If/Else Statements and their syntax 
# - While loops and its syntax 
# - The print statement and its formatting with concatenation with other variables
# - Indentation style syntax formatting

#* Needed for calculating random numbers
import random

#* Parameters (1, 100) to show lower and upper bounds of generating random ints
randomNumber = random.randint(1, 100)

gameDone = False

print("Welcome to the number guessing game! I'll think of a random number 1-100, and you'll"
      + "\ntry guessing it! I already thought of my number, so go ahead!")

while gameDone == False:
    usersGuess = int(input("\n\nEnter a number 1-100. If you give up, enter 0: "))
    
    #? Conditional for quitting the game
    
    if usersGuess == 0:
        print("\n\nToo bad! My guessed number was " + str(randomNumber) + "!")
        print("\nTry again sometime soon!")
        gameDone = True
    
    #? Conditional for not guessing correctly
    
    elif usersGuess > 100 or usersGuess < 1:
        print("\n\nYour guessed number was out of bounds, try again!")

    #? Conditional for winning the game
    
    elif usersGuess == randomNumber:
        print("\n\nYou correctly guessed my number! I was thinking of " + str(randomNumber) + "!")
        print("\nCongratulations, you win!")
        gameDone = True
        
    #? Conditionals for guessed number
    
    elif usersGuess < randomNumber:
        print("\n\nYour guessed number " + str(usersGuess) + " is LOWER than my number! Try again")
        
    elif usersGuess > randomNumber:
        print("\n\nYour guessed number " + str(usersGuess) + " is HIGHER than my number! Try again")
