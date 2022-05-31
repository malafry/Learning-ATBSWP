# The Collatz Sequence (Chapter 3, Project 1)
# Source: Automate the Boring Stuff With Python

# Defining the function
def collatz(number):
    if number % 2 == 0: # Determines if number is even, using modulo
        print("The number you entered, " + str(number) + ", is even!")
        print(number / 2) # UNEXPECTED: A float is printed. Why?
    elif number % 2 == 1: # Determines if number is odd, using modulo
        print("The number you entered, " + str(number) + ", is odd!")
        print(3 * number + 1)
    else:
        print("I'm uncertain what happened...") # Should never be printed, why was it? 

# Input request, running function, and ValueError exception
print("What is your number?")
try:
    number = int(input())
    collatz(number)
except ValueError:
    print("Your input cannot be used in the function. Please use numerals.")
