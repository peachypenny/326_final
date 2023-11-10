def start_game():
    name = input("Enter your name: ")
    
    game_introduction = f"Hi {name}, welcome to wordle. Here's how you play the game: "
    
    game_rule = f"You have 6 tries to guess a 5 letter word"
    
    word_gray = f"If the letter in the guessed word is gray, that means that the letter is not in the word"
    
    word_yellow = f"If the letter in the guessed word is yellow, that means that the letter is in the word but not in the correct position"
    
    word_green = f"Last but not least, if the letter in the guessed word is green, that means that the letter is in the correct position"
    
    return name + "/n" + game_introduction + "/n" + word_gray + "/n" + word_yellow + "/n" + word_green

    
    
