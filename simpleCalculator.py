# Date: 12/24/2024 | STATUS: COMPLETE

# Project: 
#     A simple calculator program that utilizes functions to find and calculate operations between 2 user-chosen number values.

# What I learned:
# - Simple 'def'/functions and how they work/look in Python
# - Return statements in Python
# - 'try' and 'except' and their handling in Python
# - Python membership testing / 'in' operation
# - More complicated concatenation syntaxing in print statements
# - Nested if/elif statements

#* Mathematical Functions that return the result of said operation

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    #* Account for division by 0
    
    if b == 0:
        return "Error: Division by 0 found. Undefined answer."
    
    return a / b

#* Calculator function to handle all main calculation logic

def calculator():
    print("Let's begin the calculations!")
    
    calculatorToggle = True
    
    while calculatorToggle == True:
        print("\nSelect an operation to perform:")
        print("\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Quit Calculator")
        
        userChoice = input("\n\nWhat would you like to do? Select a choice 1-5: ")
        
        if userChoice == '5':
            print("\nExiting the calculator. See you soon!\n")
            calculatorToggle = False
            break
        
        #* Python membership testing
        #* using 'in' means that if a variable is found within a certain list, then I can call it as valid or not
        
        if userChoice in ['1', '2', '3', '4']:
            try:
                firstNum = float(input("\nEnter your first number: "))
                secondNum = float(input("\nEnter your second number: "))
                
                if userChoice == '1':
                    print("\n" + str(firstNum) + " + " + str(secondNum) + " = " + str(add(firstNum, secondNum)) + "\n")
                    calculatorToggle = False
                
                elif userChoice == '2':
                    print("\n" + str(firstNum) + " - " + str(secondNum) + " = " + str(subtract(firstNum, secondNum)) + "\n")
                    calculatorToggle = False
                
                elif userChoice == '3':
                    print("\n" + str(firstNum) + " * " + str(secondNum) + " = " + str(multiply(firstNum, secondNum)) + "\n")
                    calculatorToggle = False
                
                elif userChoice == '4':
                    print("\n" + str(firstNum) + " / " + str(secondNum) + " = " + str(divide(firstNum, secondNum)) + "\n")
                    calculatorToggle = False
                
            except ValueError:
                print("\nPlease enter a valid number to perform operations with!\n\n================================")
        
        else:
            print("Please choose a valid number from the selection.")
            
# "Main Method" basically
calculator()