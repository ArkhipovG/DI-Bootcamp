from game import Game


def get_user_menu_choice():
    user_choices = ['g', 'q']
    print("(g)Play a new game")
    print("(q)Show score and quit")

    get_user_choice = input(": ")
    if get_user_choice in user_choices:
        return get_user_choice
    else:
        print("Invalid choice")


def print_results(scores):
    print(f'You won: {scores['win']} times')
    print(f'You lost: {scores['loss']} times')
    print(f'You drew: {scores['draw']} times')


def main():
    print("Welcome to Rock Paper Scissors game!")
    scores = {'win': 0, 'loss': 0, 'draw': 0}
    end = False
    while not end:
        user_choice = get_user_menu_choice()
        if user_choice == 'g':
            game = Game()
            result = game.play()
            if result == 1:
                scores['win'] += 1
            elif result == 2:
                scores['loss'] += 1
            elif result == 3:
                scores['draw'] += 1
        if user_choice == 'q':
            print_results(scores)
            print("Goodbye!")
            end = True


main()
