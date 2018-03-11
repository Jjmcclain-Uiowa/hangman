from random import randint
from sys import exit

# load word list from text file
text_file = open('wordlist.txt', 'r')
word_list = []
for line in text_file:
    word_list.append(line.strip('\n').lower())

print()
print('_______________________________________________________')
print('|Welcome to Hangman!                                  |')
print('|Type ! when guessing to see previous guesses         |')
print('|Input number of wrong guesses until death (default=6)|')
print('|Press Enter to begin.                                |')
print('|_____________________________________________________|')
print()

inp = input()
if inp.isnumeric():
    max_incorrect_guesses = inp

while True:
    # create initial variables
    already_guessed = []
    correct_letter_count = 0
    incorrect_guess_count = 0
    max_incorrect_guesses = 6

    # choose word from word_list
    chosen_word = [c for c in word_list[randint(0, len(word_list)-1)]]

    # create a display_word list to display word with _ for missing letters
    display_word = []
    for c in chosen_word:
        display_word.append('_')

    print('Your word is ' + str(len(chosen_word)) + ' letters long.')
    print(' '.join(display_word), '\n')

    # begin loop to get input, stop when word is guessed or incorrect max is reached
    while incorrect_guess_count < max_incorrect_guesses and correct_letter_count < len(chosen_word):

        # get guess
        guess = input('Guess a letter!: ')
        print()

        # print list of prev guesses if !
        if guess == '!':
            print('Previous guesses')
            print(already_guessed)
            guess = input('Guess a letter!: ')

        # make sure guess is a single letter
        while len(guess) != 1 or not guess.isalpha():
            if len(guess) < 1:
                guess = input('No guess. Guess a letter: ')
            if len(guess) > 1:
                guess = input('Please only guess a single letter: ')
            if not guess.isalpha():
                guess = input('You have not entered a letter.  Please guess a letter: ')

        # check if guessed already
        guess = guess.lower()
        while guess in already_guessed:
            guess = input('You have already guessed that letter! Guess a new one: ')

        already_guessed.append(guess)

        # find where in the word the guess is
        correct_indexes = []
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                correct_indexes.append(i)
                correct_letter_count += 1

        # show correct letters in display_word
        for index in correct_indexes:
            display_word[index] = guess

        # if guess is not in word, increment incorrect count
        if len(correct_indexes) == 0:
            incorrect_guess_count += 1
            print('Incorrect guess.  You have ' + str(max_incorrect_guesses - incorrect_guess_count) + ' guesses left')

        # correct guess
        elif len(correct_indexes) == 1:
            print('There was 1 ' + guess)
        else:
            print('There were ' + str(len(correct_indexes)) + ' ' + guess)

        print(' '.join(display_word))
        print('\n\n')

    # too many incorrect guesses
    if incorrect_guess_count >= max_incorrect_guesses:
        print('You are dead x_x')
        print('The correct word was ' + ''.join(chosen_word))

    # winner!
    if correct_letter_count >= len(chosen_word):
        print(''.join(display_word))
        print('You are a Winner!')

    # play again?
    inp = input('Play again? y/n: ')
    if inp == 'n':
        exit(0)





