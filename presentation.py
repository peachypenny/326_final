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