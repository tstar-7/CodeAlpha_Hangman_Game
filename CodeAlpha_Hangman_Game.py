import random
def making_guess():
    x = 0
    global update_screen
    cor_guess = False
    for letter in choose_word:
        if guess.lower() == choose_word[x]:
            blank_list[x] = guess.lower()
            cor_guess = True
        x += 1
    if cor_guess == False:
        print(f"Umm no {guess}, sorry.")
        update_screen += 1
    x = 0
 
HANGMAN= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["jeyuso", "rhearipley", "romanreigns", "codyrhodes", "tstar"]
choose_word = list(random.choice(word_list))
blank = ""
for letter in choose_word:
    blank += "_"
blank_list = list(blank)
update_screen = 0
 
#--------------------------------------------------------------------------
print(HANGMAN[update_screen])
guess = input(f"Welcome to Hangman Game.\n{blank}\n Start with a guess? ")
making_guess()
print(HANGMAN[update_screen])
print(''.join(blank_list))
while update_screen < 6:
    if blank_list == choose_word:
        print("!!! YOU WIN !!!")
        break
    guess = input("Make another guess? ")
    making_guess()
    print(HANGMAN[update_screen])
    print(''.join(blank_list))
if update_screen == 6:
    print("!!!! GAME OVER !!!!")
    