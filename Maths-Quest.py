#the program teaches children multiplication tables
#ask the user for the name and what times table they want to use
name = input("Welcome to Maths Quest! What's your name?\n")
x = int(input( name + ", which times table would you like to practice? \n"))

print("Okay " + str (name) + ": on a piece of paper, write down the " +str (x) + " times table from 1 to 12.\n When you are ready I'll show you the answer so you can check your work.")
y =input("are you ready to start?(Y/N)\n")
if y == "y":
    print("Let's begin! Write down your answers now.")
    #give time for the user to write in the answers
elif y != "y":
    input("press 'Enter' when you are ready to begin.")
import time
time.sleep(5)
    
z = input("are you ready for the answers?(Y/N)")
if z == "y":
    print("Let's see how you went!")
elif z =="n":
    input("Press 'Enter' when you are ready to see the answers.")

    #calculate the given number up to a multiple of 12
for i in range (1,13):
    print(x, "x", i, "=", x*i)
l = input("Did you get them all correct?(Y/N)")
if l == "n":
    print("Don't give up, keep practicing!")
else:
    print("Great job! Thanks for playing Maths Quest!")
exit()
