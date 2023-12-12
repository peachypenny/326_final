import random
import argparse
import pandas as pd
import re

#Anisha's method 
def get_user_info():
    """Gets the user's name and prints the game's instructions.
    
    Author: Anisha Bahl
    Technique: F-strings
    
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
        """Prints a message that indicates saving the game state.
        
        Side effects:
            Prints a statement to the console.
        """
        print("Saving game state...")
    
    """
    Penelope worked on see_leaderboard and score_leaderboard.
    Resources I used:
    - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
    - https://stackoverflow.com/questions/17695456/why-does-python-3-need-dict-items-to-be-wrapped-with-list
    """ 

    def see_leaderboard(self, filepath):
        """Displays the leaderboard containing the players and their scores.

        Args:
            filepath (str): The path to the csv file containing a table of names
                and scores.
        
        Side effects:
            Prints to the console if the csv file is not found.
        
        Retuns:
               None
        """
        try:
            leaderboard_df = pd.read_csv(filepath)
            self.scores = leaderboard_df.set_index('Name')['Score'].to_dict()
        except:
            print("File wasn't found or other error! Please try again with a new filepath.")

    def update_leaderboard(self, filepath, player_name, player_score):
        """Updates the scores of players on the leaderboard.
        
        Author: Aliyah Viray
        Resource: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
            Convert a Pandas Dataframe into a CSV.
        
        Args:
            filepath (str): The path to the csv file containing a table of names
                and scores.
            player_name (str): The player's name.
            player_score (int): The player's score.
        """
        self.scores[player_name] = player_score
        self.save_game_state()
        
        leaderboard_df = pd.DataFrame(list(self.scores.items()), columns=['Name', 'Score'])
        leaderboard_df.to_csv(filepath, index=True)


    def get_player_score(self, player_name):
        """Retrieves the player's score.

        Args:
            player_name (str): The player's name.

        Returns:
            int: The player's score.
        """
        return self.scores.get(player_name, 0)

    def update_player_score(self, player_name, points):
        """Updates the player's score after every guess.
        
        Authors: Anisha Bahl
        Technique: Optional parameters
        
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
    
        Author: Anisha Bahl and Penelope Newcomb
        Technique: Use of a key function
        
        Returns:
             pd.DataFrame: A Pandas DataFrame containing the top 3 scores.
        """
        print("Generating leaderboard...")
        leaderboard_df = pd.DataFrame(list(self.scores.items()), columns=['Name', 'Score'])
        find_top_3 = sorted(leaderboard_df.values, key=lambda x:x[1], reverse=True)[:3]
        return pd.DataFrame(find_top_3)
    
# Player Class
class Player:
    """Represents a Player in the Worldle Game.
    
    Attributes:
        name (str): The player's name
        score_manager (ScoreManager): The ScoreManager object.
        total_score (int): The player's total score.
    """
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
        """Updates the player's score if guessed within the max number of attempts.

        Author: Penelope
        Technique: Set operations on sets or frozensets
        
        Args:
            word_to_guess (str): The word that the player needs to guess.
            guesses (set): A set of guessed letters.
            attempts_left (int): The number of attempts left.

        Returns:
            str: Returns a message based on whether the player guesses correctly
                or incorrectly.
        """
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
        
#Class WordleGame 
class WordleGame:
    """Represents the Wordle Game.
    
    Attributes:
        words (list): A list of the guess words from the text file.
        filepath (str): The filepath to the text file containing the words
            for the game.
    """
    def __init__(self, filepath='wordle_words.txt'):
        """Initializes the WordleGame class.

        Args:
            filepath (str, optional): The filepath to the text file containing
                the words for the game. Defaults to 'wordle_words.txt'.
        
        Side effects:
            Initializes the attributes for the WordleGame object.
        """
        self.words = []
        self.filepath = filepath
        self.load_words()

    def load_words(self):
        """Loads the words from our text file and stores them in a list.
        
        Author: Aliyah Viray
        Techniques: `with` statement and list comprehension
        
        Side effects:
            Opens a file, reads a file, and strips the words from file of
                whitespace. Modifies a list of words if the word has 5 letters.
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.words = [line.strip() for line in file if len(line.strip()) == 5]

    def get_random_word(self):
        """Retrieves a random word from the list of words.

        Returns:
            str: A randomly selected 5-letter word.
        """
        return random.choice(self.words)
    
    def check_guess(self, secret_word, user_guess):
        """Checks whether a player's guess matches the secret word. The game
                returns feedback with corresponding colors based on the player's
                letter guesses.
               
	    Author: Salma Tagnaouti 
        Technique: Conditional expressions
        Sources:
            https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803
            https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
            In the conditional expression statement under the feedback loop,
                ANSI escape color codes were used to add color formatting to the
                guess feedback printed to the console.
      
        Args:
            secret_word (str): The random word that was selected
            user_guess (str): The player's guessed word.

        Returns:
            list: The colored feedback on the player's guess.
        """
        feedback = []
        for i in range(len(secret_word)):
            #ANSI escape codes for green, yellow, and gray texts
            feedback.append('\033[92m' + 'green' + '\033[0m' if user_guess[i] == secret_word[i] else 
                       '\033[93m' + 'yellow' + '\033[0m' if user_guess[i] in secret_word else
                       '\033[90m' + 'gray' + '\033[0m')
        return feedback
  
    def check_guess_format(self, user_guess):
        """Checks if the user's guess matches the expected format.
	
	    Author: Salma Tagnaouti
        Technique: Regular expressions
        
        Args:
            user_guess (str): The user's guessed word.

        Returns:
           bool: True if the format is valid, False otherwise.
        """
        guess_regex = r'^[a-zA-Z]{5}$' 
        if not re.match(guess_regex, user_guess):
            return False
        return True
   
    def play_round(self, player):
        """Plays a round of the Wordle game.
        
        Author: Sriya Kandula
        Technique: ANSI color codes
        Sources:
            https://replit.com/talk/learn/ANSI-Escape-Codes-in-Python/22803
            https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
                The green color is applied to specific feedback text indicating
                correct letter guesses in the player's input, enhancing the
                visual presentation of the game output.
                
        Args:
            player (Player): An instance of the Player Object.
          
        Side effects:
            Prints a message to the console based on whether the player guessed
                the word correctly or incorrectly within the given number of
                attempts.
        
        Returns:
            None
        """
        secret_word = self.get_random_word()
        guessed_correctly = False
        attempts_left = 6
        guesses = set()

        while not guessed_correctly and attempts_left > 0:
            user_guess = input("Enter your guess (5 letters): ").lower()
          
            if not self.check_guess_format(user_guess):
                print("Invalid guess format. Must be 5 letters.")
                continue
          
            if len(user_guess) == 5 and user_guess.isalpha():
                feedback = self.check_guess(secret_word, user_guess)


                for i in range(len(user_guess)):
                    letter = user_guess[i]
                    color = feedback[i]
                    #This checks if the color variable contains the green colored text "green".
                    if color == '\033[92m' + 'green' + '\033[0m':
                        guesses.add(letter)


                print("Feedback:", end=" ") 
                for f in feedback:
                    print(f, end=" ")
                print()
              
                guessed_correctly = all(color == '\033[92m' + 'green' + '\033[0m' for color in feedback)


                if guessed_correctly:
                    print(f"Congratulations, {player.name}! You guessed the word!")
                else:
                    attempts_left -= 1
                    print(f"Attempts left: {attempts_left}")
            else:
                print("Invalid input. Please enter a 5-letter word with only alphabetical characters.")


        player.game_scores(secret_word, guesses, attempts_left)
   
def main():
    """Runs the Wordle game.
    
    Author: Sriya Kandula
    Technique: ArgumentParser class
  
    Side effects:
        Prints messages to the console with the player's total score after
            they choose to end the game.
    """
    name = get_user_info()
    score_manager = ScoreManager() 
    player = Player(name, score_manager)

    parser = argparse.ArgumentParser(description='Wordle Game')
    parser.add_argument('filepath', type=str, default='wordle_words.txt', help='Path to the words file')
    parser.add_argument('leaderboard_filepath', type=str, default='leaderboard_filepath.csv', help='Path to the leaderboard file')
    args = parser.parse_args()
    score_manager.see_leaderboard(args.leaderboard_filepath)

    wordle_game = WordleGame(args.filepath)

    play_again = 'yes'
    while play_again.lower() == 'yes':
        wordle_game.play_round(player)
        play_again = input("Do you want to play again? (yes/no): ")

    score_manager.score_leaderboard()
    print(f"Thanks for playing, {player.name}! Your total score is: {player.total_score}. Goodbye!")


if __name__ == "__main__":
   main()