import random
import json

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
    
    with open(filepath, 'r', encoding = 'utf-8') as file:
        for line in file:
            self.words = [line.split() for word in file if len(word) == 5]
    
def get_random_word(self):
    return random.choice(self.words)

#Salma's methods 
 def get_feedback(self, guess):
        """
        Get feedback for a given word in the Wordle game.

        Parameters:
        guess (str): The guessed word.

        Returns:
         feedback (str): The feedback for the guess.
        """
        # check the guessed word against the actual target word 
        # return feedback (ex: correct vs incorrect vs partial)
        pass
    
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

