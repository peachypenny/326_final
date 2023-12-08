import random
import json
import argparse
import math


class Player():
    #penelope
    """
    Allows us to track score. To be called on in the game_scores method."""
    def __init__(self, name):
         self.name = ""
         self.score = 0
         self.total_score = 0

#Anisha's method 
    def start_game():
        name = input("Enter your name: ")
        game_introduction = f"Hi {name}, welcome to wordle. Here's how you play the game: "
        game_rule = f"You have 6 tries to guess a 5 letter word"
        word_gray = f"If the letter in the guessed word is gray, that means that the letter is not in the word"
        word_yellow = f"If the letter in the guessed word is yellow, that means that the letter is in the word but not in the correct position"
        word_green = f"Last but not least, if the letter in the guessed word is green, that means that the letter is in the correct position"  
        return name + "/n" + game_introduction + "/n" + word_gray + "/n" + word_yellow + "/n" + word_green

#Aliyah's methods
def __init__(self, filepath):
    self.words = []
    self.winners = []
    #penelope - we're gonna need to have more stuff in here, name =/= player?    
    with open(filepath, 'r', encoding = 'utf-8') as file:
        for line in file:
            self.words = [line.split() for word in file if len(word) == 5]
    
def get_random_word(self):
    return random.choice(self.words)

# Sriyas method
def check_guess(secret_word, user_guess):
    feedback = []
    for i in range(len(secret_word)):
        if user_guess[i] == secret_word[i]:
            feedback.append('green')
        else:
            feedback.append(None)  
    for i in range(len(secret_word)):
        if feedback[i] is None and user_guess[i] in secret_word and user_guess[i] != secret_word[i]:
            feedback[i] = 'yellow'
            feedback.extend(['black'] * (len(secret_word) - len(feedback)))

#Salmas Methods
def get_feedback(self, guess, word):
        """
        Get feedback for a given word in the Wordle game.

        Parameters:
        guess (str): The guessed word.
        word (str): The word you need to guess. 

        Returns:
         feedback (str): The feedback for the guess.
        """
        # check the guessed word against the actual target word 
        # return feedback (ex: correct vs incorrect vs partial)
    feedback = []
    for i in range(len(guess)): 
        if guess[i] == word[i]:
            feedback.append('correct')
        elif guess[i] in word:
            feedback.append('misplaced')
        else:
            feedback.append('wrong')
    return feedback
    
def save_game_state(self, filename="game_state.json"):
        """
        Save the current game to a JSON file.

        Parameters:
         filename (str): The name of the file to save the state of the game to. 
        """
        game_state = {
            "word_to_guess": self.word_to_guess,
            "guesses": self.guesses,
            # other information 
        }

        # use json.dump() to save the game state to a JSON file
        with open(filename, "w") as file:
            json.dump(game_state, file)
            
     # Sriyas Method
def get_user_input():
    parser = argparse.ArgumentParser(description='Wordle Game - Guess a Letter')
    parser.add_argument('guess', type=str, help='Enter your letter guess')
    args = parser.parse_args()

#penelope
def game_scores(self):
     if set(self.word_to_guess) <= self.guesses:
          print ("Yay! May need to add f string here as well depending on how we wanna set it up")
          self.Player.score += 1
          self.Player.total_score += 1
          return "Congrats" # do we want to have return + print?
     elif self.attempts_left == 0:
          print("Ran out of guesses. --> the word was: EXPR")
          return "Loser :/"
     else:
          return "Don't give up, you got this!"
      
#Anisha
def score_leaderboard(self):
        leaderboard = f"{name}: {self.get_player_score}"
        return leaderboard
