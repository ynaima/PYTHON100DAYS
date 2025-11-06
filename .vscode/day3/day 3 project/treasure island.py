print('''                                                                      ___   ___                                        
 /__  ___/                                                                  / /                                           
   / /   __      ___      ___      ___               __      ___           / /     ___     //  ___       __      ___   /  
  / /  //  ) ) //___) ) //   ) ) ((   ) ) //   / / //  ) ) //___) )       / /    ((   ) ) // //   ) ) //   ) ) //   ) /   
 / /  //      //       //   / /   \ \    //   / / //      //             / /      \ \    // //   / / //   / / //   / /    
/ /  //      ((____   ((___( ( //   ) ) ((___( ( //      ((____       __/ /___ //   ) ) // ((___( ( //   / / ((___/ /''')

print("\n")

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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************\n''')


#greetings
print("Welcome to the Treasure Island.\nYour mission is to find the treasure.")

#first choice
choice1= input("You are at a cross road. Where do you want to go?\n\t Type 'left' or 'right'\n")

if choice1.lower() == "left":
    choice2 = input("You come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if choice2.lower() == "wait":
       choice3=input("You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?\n")

       choice3 = choice3.lower()

       if choice3 == "red":
              print("It's a room full of fire. Game Over.")
       elif choice3 == "yellow":
              print("You found the treasure! You Win!")
       elif choice3 == "blue":
              print("You enter a room of beasts. Game Over.")
       else:
              print("You chose a door that doesn't exist. Game Over.")
    else:
       print("You get attacked by an angry trout. Game Over.")

    
else:
    print("You fell into a hole. Game Over.")

    

