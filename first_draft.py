import random
import argparse
import pandas as pd

#Anisha's method 
def get_user_info():
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
        self.scores = {}
    """
    Penelope worked on see_leaderboard and update_leaderboard.
    Resources I used:
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
    - https://stackoverflow.com/questions/17695456/why-does-python-3-need-dict-items-to-be-wrapped-with-list
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
    """ 
    def see_leaderboard (self, filepath):
        try:
            leaderboard_df = pd.read_csv(filepath)
            self.scores = leaderboard_df.set_index('Name')['Score'].to_dict()
        except:
            print("File wasn't found or other error! Please try again w/ new filepath.")
    def update_leaderboard (self, filepath, player_name, player_score):
        self.scores[player_name] = player_score
        self.save_game_state()
        
        leaderboard_df = pd.DataFrame(list(self.scores.items()), columns=['Name', 'Score'])
        leaderboard_df.to_csv(filepath, index=True)

         #someone else did init, save_game_state, update_player_score, score_leaderboard, get_player_score
    
class Player():
    #penelope
    """
    Allows us to track score. To be called on in the game_scores method."""
    def __init__(self, name):
         self.name = ""
         self.score = 0
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



class WordleGame:
#Aliyah's methods
    def __init__(self, filepath):
        self.words = []
        self.winners = []
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
    
    
class ScoreManager:
    def __init__(self):
        self.scores = {}
        
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
            
  #Sriyas Methods          
def get_player_score(self, player_name):
        return self.scores.get(player_name, 0)
    
def update_player_score(self, player_name, points):
        current_score = self.get_player_score(player_name)
        new_score = current_score + points
        self.scores[player_name] = new_score
        self.save_scores()
            
     # Sriyas Method
def get_user_input():
    parser = argparse.ArgumentParser(description='Wordle Game - Guess a Letter')
    parser.add_argument('guess', type=str, help='Enter your letter guess')
    args = parser.parse_args()

"""
#Anisha
def score_leaderboard(self):
    leaderboard = f"{name}: {self.update_player_score()}"
    return leaderboard
"""
   
def main():
    #i think sriya did a lot of this, so fill in what you did to! don't wanna take credit for your work - penelope

    """
    Delete quotations once you've filled in the rest of the main function:
    parser.add_argument('leaderboard_filepath', type=str, default='leaderboard.csv', help='Path to the leaderboard file')
    score_manager.see_leaderboard(args.leaderboard_filepath)
    #displaying the leaderboard when player is done playing - penelope
    score_manager.score_leaderboard()
    print(f"Thanks for playing, {player.name}! Your total score is: {player.total_score}. Goodbye!")
    """