import os
from random import choice

HANGMAN_STAGES = [
    """
 -----
 |   |
     |
     |
     |
     |
=========""",
    """
 -----
 |   |
 O   |
     |
     |
     |
=========""",
    """
 -----
 |   |
 O   |
 |   |
     |
     |
=========""",
    """
 -----
 |   |
 O   |
/|\  |
     |
     |
=========""",
    """
 -----
 |   |
 O   |
/|\  |
 |   |
     |
=========""",
    """
 -----
 |   |
 O   |
/|\  |
 |   |
/ \  |
========="""

]

def get_words():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "words.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().splitlines()

words = get_words()

def choose_random_word(words):
    word = choice(words)
    return word

# word = choose_random_word(words)
# print(word)

def create_mask(word):
    mask = ["_"] * len(word)
    return mask

def open_letter(word, mask, letter):
    for i, char in enumerate(word):
        if char == letter:
            mask[i] = letter
    return mask

def is_word_guessed(mask):
    return "_" not in mask

def present_word(mask):
    result = " ".join(mask)
    return result

def process_letter(word, mask, letter, used_letters, count_errors):
    if letter not in used_letters:
        used_letters.add(letter)
        if letter in word:
            mask = open_letter(word, mask, letter)
        else:
            count_errors += 1
    return mask, used_letters, count_errors

RUSSIAN_LETTERS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя".upper()
def is_valid_input(letter):
    if len(letter) != 1:
        return False
    if not letter.upper() in RUSSIAN_LETTERS:
        return False
    return True

def play_round(words):
    word = choose_random_word(words)
    used_letters = set()
    count_errors = 0
    mask = create_mask(word)
    while not is_word_guessed(mask) and count_errors < 6:
        print(present_word(mask))
        print(HANGMAN_STAGES[count_errors])
        letter = input().upper()
        if is_valid_input(letter):
            mask, used_letters, count_errors = process_letter(word, mask, letter, used_letters, count_errors)
        else:
            print("Невалидный ввод")
    if is_word_guessed(mask):
        print("Вы победили!")
    else:
        print(f"Вы проиграли! Загаданное слово было: {word}")