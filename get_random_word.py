import random

def __init__(self, filepath):
    self.words = []
    
    with open(filepath, 'r', encoding = 'utf-8') as file:
        for line in file:
            self.words = [line.split() for word in file if len(word) == 5]
    
def get_random_word(self):
    return random.choice(self.words)

