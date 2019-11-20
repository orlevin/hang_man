import random

def check_valid_input(letter_guessed, old_letters_guessed):
    is_one_char = len(letter_guessed) == 1
    is_alpha_char =  letter_guessed.isalpha()
    old_letters_guessed = list(old_letters_guessed)
    return is_one_char and is_alpha_char and (not (letter_guessed in old_letters_guessed))


MAX_TRIES = 6
HANGMAN_ASCII_ART="""    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/"""


def main():
    print(HANGMAN_ASCII_ART,"\n",MAX_TRIES)
    letter_guessed = input("Guess a letter:").lower()
    if is_valid_input(letter_guessed):
        print(letter_guessed)


#if _name_ == "_main_":
main()