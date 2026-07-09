import random

# List of predefined words
words = ["python", "apple", "computer", "house", "garden"]

# Select a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect:
    # Display the word with underscores for unguessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Check if the word is fully guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong!")

# If player runs out of guesses
if incorrect_guesses == max_incorrect:
    print("\nGame Over! The word was:", word)
