#Auther Liam Leeder 472792180
#Date 18/10/2021
#Version 1
#
#Rock, Paper, Scissors
#Two players

#Welcome and ask players their name

print ("Welcome to Rock, Paper, Scissors")
print(" Let's begin")
name1 = input("player 1: What's your name?")
name2= input("\n Player 2: What's your name?")

#ask the players to choose between rock, paper and scissors
print("Hello " + name1 + " and " + name2)
print(name2 + ": close you eyes!")
choice1 = input(name1 + ":Now enter 'r' for rock, 'p' for paper, and 's' for scissors: ")
print("Great choice!: Now - cover yours anser and ask " + name2 + "to choose. \n\n\n\n\n\n\n")
choice2 = input(name2 + ":Now enter 'r' for rock, 'p' for paper, and 's' for scissors: ")

#The code goes through a sequence to decide who wins
if choice1 == choice2:
    print("It's a Tie!")
elif choice1 == 's'and choice2 == 'p':
    print(name1+" wins!")
elif choice1 == 'r' and choice2 == 's':
    print(name1+" wins!")
elif choice1 == 'p' and choice2 == 'r':
    print (name1 +" wins!")
else:
    print(name2 +" wins!")
    
print(" Thanks for playing Rock, Paper, Scissors")