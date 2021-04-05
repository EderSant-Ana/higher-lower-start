from art import logo, vs
from game_data import data
from random import randint
from replit import clear

print(logo)
score = 0

def formatter_game(a, b):
  print(f"Compare A: {data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}")
  print(vs)
  print(f"Against B: {data[b]['name']}, a {data[b]['description']}, from {data[b]['country']}")

def more_followers(a, b, guess):
  global score
  if data[a]['follower_count'] > data[b]['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'

should_continue = True

b = randint(0, len(data)-1)

while should_continue:
  a = b
  b = randint(0, len(data)-1)

  while a == b:
    b = randint(0, len(data)-1)

  formatter_game(a, b)
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  is_correct = more_followers(a, b, guess)

  clear()
  print(logo)

  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}.")    






