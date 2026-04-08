import random

def hangman():
    words = ["apple", "banana", "tiger", "chair", "robot"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    used_letters = []

    print("Welcome to Hangman Game!")
    
    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        letter = input("Guess a letter: ").lower()

        if letter in used_letters:
            print("You already guessed that letter!")
            continue

        used_letters.append(letter)

        if letter in word:
            print("Correct Guess!")
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            print("Wrong Guess!")
            attempts -= 1

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame Over! The word was:", word)

hangman()
