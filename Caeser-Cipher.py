#Author: Liam Leeder
#date 10/06/2022


import re
from string import digits
# Type a mesage
text = input("what is you message? ",)
def convert_to_caeser(text):
   

    return text
def encrypt_Caesar(text,shift):
    result = ""
    

    #only looks for specified characters
    NoChar = re.sub(r"[^a-zA-Z.]","",text)

    #make the mesage uppercase, replace spaces and full stops
    text = (NoChar.upper().replace(".", "X"))


    for a in text:


        # locate positioning for the letters in the alphabet (0-25)
        Alpha  = ord(a)

        move = ord(a) + ord("A")

        # execute the shifting of letters
        new_move = (move + shift) % 26

        # encrypt the new letter
        new_Alpha = new_move + ord("A")

        new_position = chr(new_Alpha)

        # form the full encrypted message
        result = result + new_position
    return result

while True:
    shift = int(input("How many shifts?: "))
    try:
        shift = int(shift)
        break
    except ValueError:
        print("choose a number")
        pass

#Bob's your unlce. it a caesar cipher
print(encrypt_Caesar(text,shift))



#Test Area
if (encrypt_Caesar('This is finished', 3) == 'WKLVLVILQLVKHG'):
    print("Test 1 success")
else:
    print("Test Failed")
if (encrypt_Caesar('This is finished', 3) == 'WKLVLVILQLVKHG'):
    print("Test 1 success")
else:
    print("Test Failed")
          
if (encrypt_Caesar('WKLVLVILQLVKHG', -3) == 'THISISFINISHED'):
    print("Test 1 success")
else:
    print("Test Failed")
if (encrypt_Caesar('3rd test case ', 3) == 'UGWHVWFDVH'):
    print("Test 1 success")
else:
    print("Test Failed")
if (encrypt_Caesar('a shift of 3 hundred', 300) == 'OGVWTHCTVIBRFSR'):
    print("Test 1 success")
else:
    print("Test Failed")
if (encrypt_Caesar('OGVWTHCTVIBRFSR', -300) == 'ASHIFTOFHUNDRED'):
    print("Test 1 success")
else:
    print("Test Failed")
