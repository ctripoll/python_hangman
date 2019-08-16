import random


def hangman(word):
    num_wrong = 0
    stages = ["",
              "_________       ",
              "|       |       ",
              "|       |       ",
              "|       O       ",
              "|      /|\      ",
              "|      / \      ",
              "|               "
              ]
    letters = list(word)
    all_guesses = []
    board = ["__"] * len(word)
    did_win = False
    print("Welcome to Hangman!")
    while num_wrong < len(stages) - 1:
        print("\n")
        message = "-> Guess a letter (a-z): "
        char = input(message)
        if char not in all_guesses:
            if char in letters:
                indices = [i for i, c in enumerate(letters) if c == char]
                for index in indices:
                    board[index] = char
                    letters[index] = '$'
            else:
                print("\nIncorrect")
                num_wrong += 1
            all_guesses.extend(char)
        else:
            print("\nYou already guessed " + str(char))
        print(" ".join(board))
        e = num_wrong + 1
        print("\n".join(stages[0:e]))
        print("\nPrevious guesses: " + ", ".join(str(g) for g in all_guesses))
        if "__" not in board:
            print("\nYou win!")
            print(" ".join(board))
            did_win = True
            break
    if not did_win:
        print("\n".join(stages[0:num_wrong]))
        print("\nYou lose! The word was {}".format(word))


word_list = []
with open('../data/word_list.txt', "r") as file:
    for line in file:
        word_list.extend(line.split())
num = random.randint(0, len(word_list) - 1)
hangman(word_list[num])
