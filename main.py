import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors] # 2D list with variables content

user_choice = int(input("What do you choose? Type 0 or Rock, 1 for Paper or 2 for Scissors.\n"))

# If you specify a number that's equal to 3 or below 0
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

else:
    print(game_images[user_choice]) # Picks an image

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice]) # Picks an image

    # If you pick rock and cpu scissors
    if user_choice == 0 and computer_choice == 2:
        print("You win!")

    # If computer picks rock and you pick scissors
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")

    # If the computer's choice is higher than yours
    elif computer_choice > user_choice:
        print("You lose!")

    # If your choice is higher than the computers
    elif user_choice > computer_choice:
        print("You win!")

    # If both parties picked the same option
    elif computer_choice == user_choice:
        print("It's a draw!")
