print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("As you disembark from your ship, you find yourself at a fork in the road. Do you go left or right?")

path = input().lower()

if path == "left":
    print("You come across a clearing. In the distance, you see a large tree. It's said that the tree holds the key to finding the treasure.")
    print("Do you wait and search the tree for clues or continue on your journey?")
    path = input().lower()
    if path == "wait":
        print("After searching the tree, you find a small key hidden in a knot in the trunk.")
        print("Do you use the key to open the yellow door in the distance or leave it and continue on your journey?")
        path = input().lower()
        if path == "open the door":
            print("You use the key to open the door and find yourself in a large cavern.")
            print("In the center of the cavern, you see a chest filled with gold and jewels.")
            print("Congratulations! You've found the treasure of Captain Flint!")
        else:
            print("Game over. You should have used the key to open the yellow door. Better luck next time.")
    else:
        print("Game over. You should have waited and searched the tree for clues. Better luck next time.")
else:
    print("Game over. You should have gone left and searched the tree for clues. Better luck next time.")

