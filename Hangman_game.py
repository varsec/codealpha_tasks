
import random

# Step 1: Define a list of 5 predefined words
word_list = ["apple", "banana", "grape", "orange", "mango"]

# Step 2: Randomly choose a word from the list
chosen_word = random.choice(word_list)

# Step 3: Create a display list with underscores
display = ["_"] * len(chosen_word)

# Step 4: Set number of allowed incorrect guesses
max_attempts = 6
wrong_guesses = 0

# Step 5: Create a list to store guessed letters
guessed_letters = []

# Step 6: Main game loop
while "_" in display and wrong_guesses < max_attempts:
    print("\nWord: " + " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_attempts - wrong_guesses} tries left.")

# Step 7: Game end condition
if "_" not in display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame over! The word was:", chosen_word)
