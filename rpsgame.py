from random import randint

moves = ["Rock", "Paper", "Scissors"]

computer = moves[randint(0, 2)]
print(computer)

player = False

while player == False:
  player = input("Rock, Paper, Scissors?: ")
  if player == computer:
    print("TIE!")
  elif player == "Rock":
    if computer == "Paper":
      print("Paper covers Rock! Computer Wins!")
    else:
      print("Rock smashes Scissors! You Win!")
  elif player == "Paper":
    if computer == "Scissors":
      print("Scissors cut Paper! Computer Wins!")
    else:
      print("Paper covers Rock! You Win!")
  elif player == "Scissors":
    if computer == "Rock":
      print("Rock smashes Scissors! Computer Wins!")
    else:
      print("Scissors cut Paper! You Win!")
  else:
    print("Not a valid move. Check your spelling!")

  player = False
  computer = moves[randint(0, 2)]