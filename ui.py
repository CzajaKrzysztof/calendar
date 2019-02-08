def print_main_menu():
    print('Menu:\n'
          '(s) shedul a new meeting\n'
          '(c) cancel an existing meeting\n'
          '(q) quick')


def get_menu_choice():
    is_answer_correct = False
    while not is_answer_correct:
        answer = input('\nYour choice: ')
        if answer not in ['s', 'c', 'q']:
            print('Menu options are "s", "c" and "q"! Try again.')
        else:
            is_answer_correct = True

    return answer
