import js

print(r'''
*******************************************************************************
          |                   |                  |                    |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""    `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"   ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# Prompt 1
choice1 = str(js.prompt('You are at a crossroad. Do you want to go "left" or "right"?')).lower()

if choice1 == "left":
    print(f"You chose: {choice1}\n")
    
    # Prompt 2
    choice2 = str(js.prompt('Now there is a river to cross. Do you want to try swimming across, or wait for a bus? Type "swim" or "wait".')).lower()
    
    if choice2 == "wait":
        print(f"You chose: {choice2}\n")
        
        # Prompt 3
        choice3 = str(js.prompt('You arrived at the destination safe and sound. Now there is a house that has a choice of 3 doors to enter. You can choose the "yellow" door, the "blue" door, or the "red" door. Type one of the colors.')).lower()
        
        print(f"You chose: {choice3}\n")
        if choice3 == "yellow":
            print('You found the treasure! You Win!')
        elif choice3 == "blue":
            print("You were eaten by beasts! Game Over.")
        else:
            print("You were burned by fire! Game Over.")
    else:
        print(f"You chose: {choice2}\n")
        print("You ran into a school of piranha fish and didn't survive. Game over.")
else:
    print(f"You chose: {choice1}\n")
    print("You triggered the booby trap and unlocked the trap door and you fell in. Game over.")
