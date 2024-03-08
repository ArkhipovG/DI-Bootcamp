import random


def draw_hangman(incorrect_guesses):
    stages = [
        """
        --------
        |      |
        |
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |      |
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     /
        |
        ----------
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     / \\
        |
        ----------
        """
    ]

    return stages[incorrect_guesses]


def check_guess(word_list, hidden_word, incorrect_guesses_list):

    is_checked = False
    while not is_checked:
        guess = input("Guess a letter: ").lower()

        if guess not in incorrect_guesses_list and guess not in hidden_word:
            for i, letter in enumerate(word_list):
                if guess == letter:
                    hidden_word[i] = guess
                    is_checked = True

            if guess not in word_list:
                print("Sorry, you are wrong")
                incorrect_guesses_list.append(guess)
                print(incorrect_guesses_list)
                is_checked = True





def check_win(hidden_word):
    if "*" not in hidden_word:
        return True


def check_lose(incorrect_guesses_list):
    if len(incorrect_guesses_list) > 5:
        return True


def play():
    is_finished = False
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'rush',
                 'south']

    word = random.choice(wordslist)

    word_list = list(word)

    hidden_word = ['*' for _ in word]

    incorrect_guesses_list = []

    incorrect_guesses = len(incorrect_guesses_list)

    print(hidden_word)
    print(word_list)
    print(draw_hangman(incorrect_guesses))

    while not is_finished:
        check_guess(word_list, hidden_word, incorrect_guesses_list)
        incorrect_guesses = len(incorrect_guesses_list)
        print(draw_hangman(incorrect_guesses))
        print(hidden_word)
        if check_win(hidden_word) or check_lose(incorrect_guesses_list):
            is_finished = True

    if check_win(hidden_word):
        print("Congratulations! You win")
    else:
        print(draw_hangman(incorrect_guesses))
        print("Sorry, you loose")


play()
