import random
from hangman_words import word_list
from hangman_art import logo, stages
print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)
word_length = len(chosen_word)

lives = 6

display = []
for _ in range(word_length):
    display += "_"
print(display)


end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
