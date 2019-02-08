import functions


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


def show_meetings(meetings_list, title, today='no'):
    MEETING_START = 3
    MEETING_LENGTH = 4
    MEETING_TITLE = 5
    print('\n' + title + ':')
    if len(meetings_list) == 0:
        print('(empty)\n')
    else:
        for entry in meetings_list:
            meeting_end = int(entry[MEETING_START]) + int(entry[MEETING_LENGTH])
            if meeting_end > 24:
                meeting_end = meeting_end - 24
            if today == 'yes':
                string = '{} - {} {}'
                formating = [entry[MEETING_START], meeting_end, entry[MEETING_TITLE]]
            else:
                meeting_date = functions.join_date(*entry[:MEETING_START])
                string = '{}-{}-{} {} - {} {}'
                formating = [meeting_date[:4], meeting_date[5:6], meeting_date[7:8], entry[MEETING_START], meeting_end, entry[MEETING_TITLE]]
            print(string.format(*formating))
        print('\n')


def simple_print(text):
    print(text)


def get_input(question):
    answer = input(question + ': ')

    return answer


def print_error(message):
    print('Error: ' + str(message))
