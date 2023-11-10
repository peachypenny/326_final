print("Hi, my name is Aliyah.")
print("Hello, my name is Anisha")
print("hey,its sriya")

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


