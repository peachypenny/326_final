import random
import argparse
import pandas as pd
import re

#Anisha's method 
def get_user_info():
    """
    Author: Anisha
    Gets the user's name and prints the game's instructions.


    Returns:
        name (str): The player's name.
       
    Side effects:
        Prints information to the console.
    """
        name = input("Enter your name: ")
        print(f"Hi {name}, welcome to Wordle. Here's how you play the game:")
        print("You have 6 tries to guess a 5-letter word.")
        print("If the letter in the guessed word is gray, that means that the letter is not in the word.")
        print("If the letter in the guessed word is yellow, that means that the letter is in the word but not in the correct position.")
        print("If the letter in the guessed word is green, that means that the letter is in the correct position.")
        return name

# Score Manager Class
class ScoreManager:
    def __init__(self):
        """Initializes the ScoreManager object.
        
        Side effects:
            Initializes the attributes for the ScoreManager object.
        """
        self.scores = {}

    def save_game_state(self):
        """
        Prints a message that indicates saving the game state.
        
        Side effects:
            Prints a statement to the console.
        """
        print("Saving game state...")
    
    """
    Penelope worked on see_leaderboard, update_leaderboard, and score_leaderboard.
    Resources I used:
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
    - https://stackoverflow.com/questions/17695456/why-does-python-3-need-dict-items-to-be-wrapped-with-list
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    """ 

    def see_leaderboard(self, filepath):

        try:
            leaderboard_df = pd.read_csv(filepath)
            self.scores = leaderboard_df.set_index('Name')['Score'].to_dict()
        except:
            print("File wasn't found or other error! Please try again with a new filepath.")

    def update_leaderboard(self, filepath, player_name, player_score):
        self.scores[player_name] = player_score
        self.save_game_state()
        
        leaderboard_df = pd.DataFrame(list(self.scores.items()), columns=['Name', 'Score'])
        leaderboard_df.to_csv(filepath, index=True)

    def get_player_score(self, player_name):

        return self.scores.get(player_name, 0)

    def update_player_score(self, player_name, points):
        """
        Authors: Anisha and Penelope
        Updates the player's score after every guess.


        Args:
            player_name (str): The player's name.
            points (int): The points to add to the player's current score.
           
        Side effects:
            Modifies the player's current score to the new score in the
                dictionary, `self.scores`.
        Returns:
              None
        """


        current_score = self.get_player_score(player_name)
        new_score = current_score + points
        self.scores[player_name] = new_score
        self.save_game_state()  

    def score_leaderboard(self):
        """Prints a message to generate the leaderboard.
        
        Returns:
             pd.DataFrame: A Pandas DataFrame containing the top 3 scores.
        """
        
        print("Generating leaderboard...")
        leaderboard_df = pd.DataFrame(list(self.scores.items()), columns=['Name', 'Score'])
        find_top_3 = sorted(leaderboard_df.values, key=lambda x:x[1], reverse=True)[:3]
        return pd.DataFrame(find_top_3)
    
# Player Class
class Player:

    def __init__(self, name, score_manager):
        """Initializes the Player object.

        Args:
            name (str): The player's name.
            score_manager (ScoreManager): An instance of the ScoreManager object.
        
        Side effects:
            Initializes attributes for the Person Object.
        """
        self.name = name
        self.score_manager = score_manager
        self.total_score = 0
        
    def game_scores(self, word_to_guess, guesses, attempts_left):

        if set(word_to_guess) <= guesses:
            print(f"Yay! {self.name}, you guessed the word!")
            self.score_manager.update_player_score(self.name, 1)
            self.total_score += 1
            return "Congrats"
        elif attempts_left == 0:
            print(f"Ran out of guesses. The word was: {word_to_guess}")
            return "Loser :/"
        else:
            return "Don't give up, you got this!"


def main():
    #i think sriya did a lot of this, so fill in what you did to! don't wanna take credit for your work - penelope
    
    parser.add_argument('leaderboard_filepath', type=str, default='leaderboard.csv', help='Path to the leaderboard file')
    score_manager.see_leaderboard(args.leaderboard_filepath)
    #displaying the leaderboard when player is done playing - penelope
    score_manager.score_leaderboard()
    print(f"Thanks for playing, {player.name}! Your total score is: {player.total_score}. Goodbye!")
