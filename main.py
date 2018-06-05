import random
from random import randint
player = input("R -> Rock , P -> Paper , S -> Scissor ?").lower()

print(player, 'v/s' , end= " ")

chosen = randint(1,3)

if chosen == 1:
    computer = 'r'
elif chosen==2:
    computer = 'p'
elif chosen==3:
    computer = 's'

print(computer)
if (player == computer):
    print("Draw")
elif(player == 'r' or player == 'R' and computer == 's'):
    print("Player Wins")
elif(player == 'r' or player == 'R' and computer == 'p'):
    print("Computer Wins")
elif(player == 'p' or player == 'P' and computer == 'r'):
    print("Computer Wins")
elif(player == 'p' or player == 'P' and computer == 's'):
    print("Computer Wins")
elif(player == 's' or player == 'S' and computer == 'p'):
    print("Player Wins")
elif(player == 's' or player == 'S' and computer == 'r'):
    print("Computer Wins")





