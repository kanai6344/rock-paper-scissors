import random
import os

class RockPaperScissors:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.options = ['rock', 'paper', 'scissors']
        
    def get_computer_choice(self):
        return random.choice(self.options)
    
    def get_user_choice(self):
        while True:
            user_choice = input("Choose rock, paper, or scissors: ").lower()
            if user_choice in self.options:
                return user_choice
            print("Invalid choice. Please try again.")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            return 'user'
        else:
            return 'computer'
    
    def display_result(self, user_choice, computer_choice, result):
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if result == 'tie':
            print("It's a tie!")
        elif result == 'user':
            print("You win!")
        else:
            print("You lose!")
        
        print(f"\nScore - Wins: {self.wins}, Losses: {self.losses}, Ties: {self.ties}")
    
    def play_round(self):
        print("\n" + "="*30)
        print("Rock Paper Scissors Game")
        print("="*30)
        
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == 'user':
            self.wins += 1
        elif result == 'computer':
            self.losses += 1
        else:
            self.ties += 1
            
        self.display_result(user_choice, computer_choice, result)
    
    def play_game(self):
        while True:
            self.play_round()
            
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                print("\nFinal Score:")
                print(f"Wins: {self.wins}, Losses: {self.losses}, Ties: {self.ties}")
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
