import sys
import random

class RPS():
    def __init__(self) -> None:
        print("Welcome to RPS")
        self.moves: dict = {"rock": "ROCK", "paper" : "PAPER", "scissor": "SCISSORS" }
        self.valid_moves: list = list(self.moves)

    def play_game(self):
        user_move = input("Enter rock, paper or scissor: ").lower()
        ai_move: str = random.choice(self.valid_moves)

        if user_move == "exit":
            print("Thanks for playing")
            sys.exit()
        
        if user_move not in self.valid_moves:
            print("Invalid move !!")
            return self.play_game()
    
        self.display_moves(user_move, ai_move)
        self.check_moves(user_move, ai_move)

    
    def display_moves(self, user_move:str, ai_move:str):
        print("-----")
        print(f"You : {self.moves[user_move]}")
        print(f"AI : {ai_move.upper()}")
        print("-----")
    
    def check_moves(self, user_move:str, ai_move:str):
        if ai_move == user_move:
            print("It's a tie")
        if ai_move == "rock" and user_move == "scissor":
            print("AI won !!!")

        elif ai_move == "scissor" and user_move == "paper":
            print("AI won !!!")

        elif ai_move == "paper" and user_move == "rock":
            print("AI won !!!")

        else:
            print("You won !!")

if __name__ == "__main__":
    rps = RPS()
    while True:
        rps.play_game()




