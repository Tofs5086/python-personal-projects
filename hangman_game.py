import random
import Hangmangame_words #imports your list of words
lives = 6 # create lives for the game
chosen_word = random.choice(Hangmangame_words.words)  # this code generates a random choice of words from your list of possible words
display = []
for i in range(len(chosen_word)):
    display += '_'       #this code will assign a blankspace to each chosen letter
print(display)
game_over = False
while not game_over:
    guessed_letter = input('Guess a letter: ').lower()  # takes an input from the user
    for position in range(len(chosen_word)):#checks whether the users's input is the correct letter and at the right position
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position]= guessed_letter #displays the correct letter at the right position
    print(display)
    if guessed_letter not in chosen_word: #checks if user does not give the right word at the right position
        lives -= 1 #loses a life
        if lives == 0: #checks if all lives are lost
            game_over = True
            print('you lose!!')
    if '_' not in display: #checks if all the blank spaces are filled with the correct letters
        game_over = True
        print('You win')