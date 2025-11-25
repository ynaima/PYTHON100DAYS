import random

print("ROCK, PAPER, SCISSORS GAME")



#users input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))




rock = '''_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper ='''_______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''


scissors = '''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

if user_choice >= 0 or user_choice <= 2:
    print(f"\nYou chose:\n{game_images[user_choice]}")

computers_choice = random.randint(0,2)
print(f"\nComputer chose:\n{game_images[computers_choice]}\n")

"""using logical operators to reduce the number of if statements and then catching the exceptions
we know that 1 beats 0, 2 beats 1.
exceptions: 0 beats 2."""




if user_choice > 2 or user_choice < 0:
    print("Invalid input! You lose!")

if user_choice == 2 and computers_choice == 0:
    print("You lose!")

elif user_choice == 0 and computers_choice == 2:
    print("You win!")

elif user_choice > computers_choice:
    print("You win!")

elif user_choice < computers_choice:
    print("You lose!")

else:
    print("It's a draw!")


