import random


def game_dictionary():
    user_variants = input()
    print('Okay, let\'s start')
    if not user_variants:
        user_variants = 'rock,paper,scissors'
    game_dic = user_variants.split(',')
    return game_dic


def check_name():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    score_dict = {}
    with open('rating.txt', 'r') as file:
        for line in file:
            (key, value) = line.split()
            score_dict[key] = value
    if name in score_dict:
        return int(score_dict[name])
    else:
        return 0


def game(game_dic2):
    global user_score
    random_entry = random.choice(game_dic2)
    user_input = input()
    if user_input == '!exit':
        return f'Bye!'
    elif user_input == '!rating':
        return f'Your rating: {user_score}'
    elif user_input in game_dic2:
        game_dic2_half_len = len(game_dic2) // 2
        user_choice_shift = game_dic2.index(user_input) - game_dic2_half_len
        game_rule_centered = game_dic2[user_choice_shift:] + game_dic2[:user_choice_shift]
        # print(game_dic2[user_choice_shift:])
        # print(game_dic2[:user_choice_shift])
        if user_input == random_entry:
            user_score += 50
            return f'There is a draw ({user_input})'
        elif game_rule_centered.index(user_input) < game_rule_centered.index(random_entry):
            return f'Sorry, but the computer chose {random_entry}'
        else:
            user_score += 100
            return f'Well done. The computer chose {random_entry} and failed'
    else:
        return f'Invalid input'


if __name__ == '__main__':
    user_score = check_name()
    game_dic1 = game_dictionary()
    while True:
        result = game(game_dic1)
        if result == 'Bye!':
            print(result)
            break
        else:
            print(result)
