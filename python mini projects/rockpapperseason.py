# Create a simple Rock, Paper, Scissors game where the player competes against the computer.
# Rules:
#  Rock beats Scissors
# . Scissors beats Paper
# . Paper beats Rock
# . Same choice = Draw
# functions:
# · get_computer_choice()
# · get_player_choice()
# · check_winner(player, computer)
# · play_game()
# · main()
import random
def get_computer_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)

def get_player_choice():
    choice=input("enter rock,paper or scissors").lower()
    return choice

def check_winner(player,computer):
    if player==computer:
        return "draw"
    elif player =="rock" and computer =="scissors":
        return "player win"
    elif player =="scissors" and computer =="paper":
            return "player win"
    elif player =="paper" and computer =="rock":
            return "player win"
    else:
         return "computer win"

def play_game():
     player=get_player_choice()

     if player not in ["rock","paper","scissors"]:
          print("invalid choice ")
          return

     computer=get_computer_choice()

     print("player choice:",player)
     print("computer choice",computer)

     result=check_winner(player,computer)
     print("result:",result)

def main():
     print("welcome to rock papper scissors")
     play_game()

if __name__ == "__main__":
     main()


         

