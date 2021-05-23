# Program Treasure Island - Day 04 of 100

import random

rock = '''
    ________
---'    ____)
        (_______)
        (_______)
____    (_______)
    '___(_______)
'''

paper = '''
    ________
---'    ____)___
            ______)
        ______________)
____    (________)
    '___(______)
'''

scissor = '''
    ________
---'    ____)___
            ____)
        __________)
____    (____)
    '___(____)
'''

game_images = [rock, paper, scissor]

print("Welcome to Rock, Paper and Scissor game")
user = int(input("What do you choose? Type '0' for Rock, '1' for Paper and '2' for Scissor.\n"))
computer = random.randint(0,2)
print(f"You selected{game_images[user]}")
print(f"Computer selected{game_images[computer]}")
if (user >= 3 or user  < 0):
    print("Invalid number...Try again!")
    exit()
elif (user == 0 and computer == 2):
    print("You WIN...GAME OVER")
elif (computer == 0 and user == 2):
    print("You LOSE...GAME OVER")
elif (user > computer):
    print("You WIN...GAME OVER")
elif (computer > user):
    print("You LOSE...Try again!")
elif (user == computer):
    print("It's a Draw...Try again!")