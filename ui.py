import functions


def print_main_menu():
    print('Menu:\n'
          '(s) shedul a new meeting\n'
          '(e) edit sheduled meeting\n'
          '(c) cancel an existing meeting\n'
          '(q) quit')


def get_menu_choice():
    is_answer_correct = False
    while not is_answer_correct:
        answer = input('\nYour choice: ')
        if answer not in ['s', 'e', 'c', 'q']:
            print('Menu options are "s", "c" and "q"! Try again.')
        else:
            is_answer_correct = True

    return answer


def default_view():
    print_main_menu()
    choice = get_menu_choice()

    return choice


def show_meetings(meetings_list, title, today='no', hours_count=False):
    """
    Print out meetings

    Params:
        meetings_list - list of lists containig
                        sheduled meetings
        today: "yes" - print meeting in format
                       for present day
               "no"(default) - print meetings 
                       in format with full date
        hours_count: True - prist total count of
                            meetings hours
                     False(default) - don't show
                            total count of meetins hours
    """
    MEETING_START = 3
    MEETING_LENGTH = 4
    MEETING_TITLE = 5

    hours_total = 0
    for entry in meetings_list:
        hours_total += int(entry[MEETING_LENGTH])

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
                formating = [meeting_date[:4], meeting_date[5:6], meeting_date[7:8],
                             entry[MEETING_START], meeting_end, entry[MEETING_TITLE]]
            print(string.format(*formating))
        print('\n')
        if hours_count:
            print('Total count of meetings hours is {}'.format(hours_total))


def simple_print(text):
    print(text)


def get_input(question):
    answer = input(question + ': ').strip()

    return answer


def print_error(message):
    print('\nERROR: ' + str(message))
