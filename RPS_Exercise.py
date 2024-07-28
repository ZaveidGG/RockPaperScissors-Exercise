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

yourChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
compChoice = random.randint(0,2)
handChoices = [rock, paper, scissors]

if (yourChoice<0 or yourChoice>=3):
    print("You have entered an invalid number.")
else:
    print(f"You have chosen {handChoices[yourChoice]}")
    print(f"Enemy has chosen {handChoices[compChoice]}")

    if yourChoice == compChoice:
        print("It resulted in a draw")
    elif (yourChoice == 0 and compChoice == 2) or (yourChoice == 2 and compChoice == 1) or (yourChoice == 1 and compChoice == 0):
        print("You have won!")
    else:
        print("You have lost!")

