from game import get_words, play_round

words = get_words()
while True:
    print("новая игра (1) или выход (2)?")
    solution = input()
    if solution == "1":
        play_round(words)
    else:
        break