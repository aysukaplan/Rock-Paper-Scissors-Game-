# This is a rock paper scissors game
import random

rock1 = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper1 = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors1 = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def printing_tie():
    print("It's a draw.")
def printing_win_human():
    print("You won.")

def printing_win_comp():
    print("Computer won.")


move = ["rock", "paper", "scissors"]
move_chars = [rock1, paper1, scissors1]
number_human = int(input("enter 0 for rock, 1 for paper and 2 for scissors "))
number_comp = random.randint(0,2)
print(f"You played {move[number_human]}")
print(move_chars[a])
print(f"Computer played {move[number_comp]}")
print(move_chars[a])
if number_human == number_comp:
    printing_tie()
elif number_human == number_comp-1:
    printing_win_comp()
elif number_comp == number_human-1:
    printing_win_human()
elif number_comp == number_human+2:
    printing_win_human()
elif number_human == number_comp+2:
    printing_win_comp()