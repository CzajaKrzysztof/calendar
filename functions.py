import ui
import storage
from datetime import datetime


def get_todays_meetings(meetings):
    today_meetings = []
    current_date = get_currnet_date()
    for meeting in meetings:
        meeting_date = join_date(*meeting[:3])
        if current_date == meeting_date:
            today_meetings.append(meeting)

    return today_meetings


def get_currnet_date():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    current_date = join_date(year, month, day)

    return current_date


def join_date(year, month, day):
    if len(str(month)) < 2:
        month = '0' + str(month)
    if len(str(day)) < 2:
        day = '0' + str(day)

    date = str(year) + str(month) + str(day)

    return date


def get_meeting_data():
    meeting_data = []
    ui.simple_print('Shedul a new meeting:')
    for question in range(6):
        is_answer_correct = False
        while not is_answer_correct:
            try:
                if question == 0:
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter meeting year', 2019, 2030)
                if question == 1:
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter meeting month', 1, 12)
                if question == 2:
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter meeting day', 1, 31)
                if question == 3:
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter starting hour', 1, 24)
                if question == 4:
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter meeting length', 1, 2)
                if question == 5:
                    is_answer_correct = handle_string_input(meeting_data, 'Enter meeting title')
            except (ValueError, TypeError, NameError) as err:
                ui.print_error(err)

    return meeting_data


def handle_string_input(meeting_data, question):
    is_answer_correct = False
    title = ui.get_input(question)
    if validate_string(title):
        is_answer_correct = True
        meeting_data.append(title)

    return is_answer_correct


def handle_digit_input(list_, question, start, end):
    is_answer_correct = False
    answer = ui.get_input(question)
    if validate_digit(answer, start, end):
        is_answer_correct = True
        list_.append(answer)

    return is_answer_correct


def validate_digit(digit, start, end):
    """
    Validate digit:
    first - is string empty
    second - if not empty is it a digit
    third - if is a digit is it in apropriet range
    """
    is_a_valid_digit = True
    if not digit:
        ui.print_error('You must enter something')
        is_a_valid_digit = False
    if digit:
        if not digit.isdigit():
            ui.print_error('It must be a digit')
            is_a_valid_digit = False
    if digit.isdigit():
        digit = int(digit)
        if not (start <= digit <= end):
            ui.print_error('Entry must be in between {} and {}'.format(start, end))
            is_a_valid_digit = False

    return is_a_valid_digit


def validate_string(string):
    is_a_valid_string = True
    if not string:
        ui.print_error('You must enter something')
        is_a_valid_string = False

    return is_a_valid_string
