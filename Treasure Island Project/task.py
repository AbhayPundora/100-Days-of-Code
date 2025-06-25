print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
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
print("Welcome to the Lost Pyramid.")
print("Your mission is to find the Crown of Eternity .")
choice1 = input('You\'re at the Entrance Hall, You find a stone tablet with ancient symbols. Two buttons are below it '
                'Press "left" or "right".\n').lower()
if choice1 == "left":
    choice2= input('This is the Hall of Statues.\nTake the "spear" or the "sword" to proceed.\n').lower()
    if choice2 == "spear":
        print("opening the hidden passage...")
        choice3 = input('You entered a maze of mirrors and crystals with three glowing paths.\nchoose "blue","read" or "green" Path.\n').lower()
        if choice3 == "blue":
            print("A fierce guardian appears!")
            choice4 = input("fierce guardian: What is more valuable, gold or knowledge?\n").lower()
            if choice4 == "knowledge":
                print("Entering to the Treasure Chamber:")
                choice5 = input("Choose the correct symbol from sun, moon, or star to claim the crown.\n")
                if choice5 == "sun":
                    print("You Won! 🥳")
                else:
                    print("You Lost!")
            else:
                print("you’re defeated by the guardian")
        elif choice3 == "green":
            print(" Loops endlessly until you starve, Game Over!")
        else:
            print("Walls collapsing!, Game Over!")
    else:
        print("Attacked by statues, Game Over! ")
else:
    print("you’re sealed in the entrance forever, Game Over!")

