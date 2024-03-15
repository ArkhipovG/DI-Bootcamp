import random


class Game:

    @staticmethod
    def get_user_item():
        items = ['r', 'p', 's']
        while True:
            user_item = input('Select (r)rock, (p)paper, (s)scissors): ')
            if user_item in items:
                return user_item
            else:
                print('Invalid select')

    @staticmethod
    def get_computer_item():
        items = ['r', 'p', 's']
        computer_item = random.choice(items)
        return computer_item

    @staticmethod
    def get_game_result(user_item, computer_item):

        if user_item == 'p' and computer_item == 'r':
            result = 1
            return result
        elif user_item == 'r' and computer_item == 's':
            result = 1
            return result
        elif user_item == 's' and computer_item == 'p':
            result = 1
            return result
        elif user_item == 'r' and computer_item == 'p':
            result = 2
            return result
        elif user_item == 'p' and computer_item == 's':
            result = 2
            return result
        elif user_item == 's' and computer_item == 'r':
            result = 2
            return result
        elif user_item == computer_item:
            result = 3
            return result
        else:
            print('Unknown Error')

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        game_result = self.get_game_result(user_item, computer_item)
                        
        if game_result == 1:
            print(
                f"You choose {user_item}, computer choose {computer_item}, Result: You won!")
        elif game_result == 2:
            print(
                f"You choose {user_item}, computer choose {computer_item}, Result: You lost.")
        elif game_result == 3:
            print(
                f"You choose {user_item}, computer choose {computer_item}, Result: draw")

        return game_result

# def print_results(results):
#     scores = {'win': 0 ,'loss': 0 ,'draw': 0}
#     if results['result'] == 1:
#         print(f"You choose {results['user_item']}, computer choose {results['computer_item']}, Result: You won!")
#         scores['win'] += 1
#     if results['result'] == 2:
#         print(f"You choose {results['user_item']}, computer choose {results['computer_item']}, Result: You lost.")
#         scores['loss'] += 1
#     if results['result'] == 3:
#         print(f"You choose {results['user_item']}, computer choose {results['computer_item']}, Result: draw")
#         scores['draw'] += 1
#     print(f'You won: {scores['win']} times')
#     print(f'You lost: {scores['loss']} times')
#     print(f'You drew: {scores['draw']} times')
