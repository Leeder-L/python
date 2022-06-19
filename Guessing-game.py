#Liam Leeder 472792180
#Date 18/10/2021
#Version 1
#
#Guess the random number game
#user vs. computer

import random
minGuess = 1
maxGuess = 6

#ask user for their name and guess
name = input("What is your name? ")
print ("Hi, " +(name))
print ("enter a number between: "  +str (minGuess) +" and "  +str (maxGuess))
guess = int(input("What''s your guess?"))

#Generate a random number and tell the user if they won or lost
secretNumber = random.randint(minGuess, maxGuess)
if (guess == secretNumber):
    print(" Pog Champ! The number was " +str (secretNumber) +"!")
else:
    print("Sadge, you lose! the number was " +str(secretNumber))

print("Thanks for playing Guess the number")

#task asked to fix lines 14, 15, 20 and 23.