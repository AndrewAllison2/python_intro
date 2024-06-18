import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Guess a number between 1 and {x}: "))
    if guess < random_number:
      print("Guess to low. Try again.")
    elif guess > random_number:
      print("Guess too high. Try again.")
  print(f"You got it! It was {random_number}")
