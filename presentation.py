#presentation file

"""
Future Features:
- save game state
class Player():
    # Allows us to track score. To be called on in the game_scores method.
    def __init__(self, name):
         self.name = ""
         self.score = 0
         self.total_score = 0
"""


class WordleGame:
    def __init__(self, filepath):
        self.words = []
        filepath = ('wordle_words.txt')
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip()
                if len(word) == 5:
                    self.words.append(word)


    def get_random_word(self):
        return random.choice(self.words)


    def check_guess(self, secret_word, user_guess):
        feedback = []
        for i in range(len(secret_word)):
            if user_guess[i] == secret_word[i]:
                feedback.append('green')
            elif user_guess[i] in secret_word:
                feedback.append('yellow')
            else:
                feedback.append('gray')
        return feedback

'''
.isalpha method was implemented with help from: 
https://www.w3schools.com/python/ref_string_isalpha.asp
'''

def play_round(self):
       secret_word = self.get_random_word()
       guessed_correctly = False
       while not guessed_correctly:
           user_guess = input("Enter your guess (5 letters): ").lower()
           if len(user_guess) == 5 and all(char.isalpha() for char in user_guess):
               feedback = self.check_guess(secret_word, user_guess)
               print("Feedback:")
               for f in feedback:
                   print(f)
               guessed_correctly = all(color == 'green' for color in feedback)
               if guessed_correctly:
                   print("Congratulations!")
               else:
                   print("Try again.")
           else:
               print("Invalid input. Please enter a 5-letter word.")

def main():
   name = get_user_info()
  
   parser = argparse.ArgumentParser(description='Wordle Game')
   parser.add_argument('filepath', type=str, help='Path to the words file')
   args = parser.parse_args()


   wordle_game = WordleGame(args.filepath)


   play_again = 'yes'
   while play_again.lower() == 'yes':
       wordle_game.play_round()
       play_again = input("Do you want to play again? (yes/no): ")


   print("Thanks for playing. Goodbye!")


if __name__ == "__main__":
   main()