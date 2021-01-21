# TO DO:
# IMPORTS: Random, game data, logo, vs
from random import randint
from game_data import data
from art import logo, vs
import os

def clear():
  os.system('cls||clear')

def check_guess(answer, a_followers, b_followers):
  if a_followers > b_followers:
    return answer == 'a'
  else:
    return answer == 'b'
print(logo) 
score = 0
game_repeat = True
person_b = data[randint(0, 49)]

while game_repeat:

  person_a = person_b 
  person_b = data[randint(0, 49)]
  while person_a == person_b:
    person_b = data[randint(0, 49)]

  # Make this one print statment. Make it a function???
  print("Compare A: " + person_a['name'] + ", a " + person_a['description'] + ", in " + person_a['country'] + ".")
  print(vs)
  print("Against B: " + person_b['name'] + ", a " + person_b['description'] + ", in " + person_b['country'] + ".")

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  a_follower_account = person_a['follower_count']
  b_follower_account = person_b['follower_count']
  is_correct = check_guess(guess, a_follower_account, b_follower_account)

  clear()
  print(logo)

  if a_follower_account > b_follower_account:
    higher_answer = "a"
  else:
    higher_answer = "b"

  if is_correct:
    score += 1
    print(f"You are right! current score: {score}")
  else:
    game_repeat = False
    print(f"You are wrong. Final score: {score}")


# if correct, move former B to A and bring in a new B

# if inccorect,  end game and show final score

# score variable that counts correct answers
# tally current score with each new matchup

# print " who has more followers? A or B " user input

# print logo (art) copy/paste or import for art.py?

# print vs (art) copy/paste or import for art.py?