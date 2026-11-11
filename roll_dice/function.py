from roll_dice.input import *

import random

num = menu()
def main():
    if num == "1":
        return start_game()

    if num == "2":
        return 2

    if num == "3":
        return 3

    if num == "4":
        print("have a nice day")
        return 

def start_game():
    player_socre = 0
    computer_score = 0
    name = input("Enter your name:  ")
    if name == "":
        print("You need to enter your name!")
    else:
        rounds = input("How many rounds do you want to play:  ")
        if rounds not in ["1","2","3","4","5","6","7","8","9","10"]:
            print("You need to choose a positive number from 1 to 10.")
        else:
            result_game = []
            sum = 0
            for i in range(int(rounds)):   
                name_win = play_round()
                n_player = name_win[1]
                n_computer = name_win[2]
                if name_win[0] ==  "player":
                    player_socre +=1
                elif name_win[0] == "computer":
                    computer_score += 1
                sum += 1
                result_game.append({"game":sum,"win":{name_win[0]},"player_s":n_player, "computer_s":n_computer})
    if player_socre > computer_score:
        winer = name
    elif player_socre < computer_score:
        winer = "computer"
    else:
        winer = "draw"
            
                    
                    

        print("================================\n"
                "----------NEW GAME----------\n"
                "================================\n"

                f"Player name:{name} \n"
                f"Number of rounds: {rounds}\n")
    for i in range(int(rounds)):
        print(  f"---------- ROUND {int(i)+1} ----------\n"

                f"{name} 🎲 {result_game[i]["player_s"]}\n"
                f"Computer: 🎲 {result_game[i]["computer_s"]}\n"

                f"{result_game[i]["win"]} wins this round!\n")

    print("================================ \n"
            "----------GAME OVER----------\n"
        "================================\n"

            f"{name}:  {player_socre} points\n"
            f"Computer: {computer_score} points\n"

            f"WINNER: {winer}!\n"

            "Game saved successfully!"
            )   


            
            
            
            


def roll_dice():
    result =  random.randint(1, 6)
    return result
    
def play_round():
    player_score = roll_dice()
    computer_score = roll_dice()
    winer = calculate_winner(player_score, computer_score)
    return winer

    
def calculate_winner(player_score, computer_score):
    if player_score > computer_score:
        win = "player"
    elif player_score < computer_score:
        win = "computer"
    else:
        win = "draw"
    return win, player_score, computer_score

def display_game_teusul():
    return 4

