import ui
import storage
from datetime import datetime
from copy import deepcopy


def get_todays_meetings(meetings):
    """ Retrive meeting only for current date. """
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


def join_date(*args):
    date = ''
    for elem in args:
        if len(str(elem)) < 2:
            elem = '0' + str(elem)
        date = date + str(elem)

    return date


def get_meeting_data(title, flag):
    """
    Asks user to input meeting data. All entered data are validated by handle functions
    with given arguments.

    Args:
        title - information what are inputs for
        flag - "all" for use in new meeting - all questions
             - "edit" for use in edit meeting - questions 1 - 4
             - "cancel" for use in canceling meeting - question 3 only
    """
    meeting_data = []
    if flag == 'all':
        count = range(6)
    elif flag == 'edit':
        count = range(4)
    elif flag == 'cancel':
        count = range(3, 4)
    ui.simple_print('\n' + title + ':')
    for question in count:
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
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter starting hour (8 to 18)', 8, 18)
                if question == 4:
                    is_answer_correct = handle_digit_input(meeting_data, 'Enter meeting length (1 or 2)', 1, 2)
                if question == 5:
                    is_answer_correct = handle_string_input(meeting_data, 'Enter meeting title')
            except (ValueError, TypeError, NameError) as err:
                ui.print_error(err)

    return meeting_data


def handle_string_input(meeting_data, question):
    """
    Ask user to provide input data and calls for validation function to chech if input is correct.
    Return True if input correct or False if not.
    """
    is_answer_correct = False
    answer = ui.get_input(question)
    if validate_string(answer):
        is_answer_correct = True
        meeting_data.append(answer)

    return is_answer_correct


def handle_digit_input(list_, question, start, end):
    """
    Ask user to provide input data and calls for validation function to chech if input is correct.
    Return True if input correct or False if not.
    """
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
    """ String can't be empty """
    is_a_valid_string = True
    if not string:
        ui.print_error('You must enter something')
        is_a_valid_string = False

    return is_a_valid_string


def validate_meeting(meeting_to_validate, meetings):
    """
    Check if meeting is in meetings list.
    Return True if given meeting date is in meetings data
    """
    result = False
    meeting_to_validate = join_date(*meeting_to_validate)
    for entry in meetings:
        meeting_date = join_date(*entry[:4])
        if meeting_to_validate == meeting_date:
            result = True

    return result


def cancel(meeting_to_delete, meetings):
    new_meetings_list = []
    meeting_to_delete = join_date(*meeting_to_delete)
    for entry in meetings:
        if not (meeting_to_delete == join_date(*entry[:4])):
            new_meetings_list.append(entry)

    return new_meetings_list


def validate_if_meeting_overlap(new_meeting, meetings):
    """
    Based on new meetings year-mont-day date construct temporary list with all
    hours of meetings. Check if hours of new meeting are in temporary list.

    Return "True" if meeting is overlapin another, "False" if is not overlaping
    """
    new_meet_copy = deepcopy(new_meeting)
    meetings_copy = deepcopy(meetings)
    MEETING_LENGTH = 4
    MEETING_HOUR = 3
    result = False
    date = join_date(*new_meet_copy[:3])
    temp_meetings_copy = []
    new_meet_copy_temp = []

    for entry in meetings_copy:
        if date == join_date(*entry[:3]):
            temp_meetings_copy.append(join_date(*entry[:4]))
            if entry[MEETING_LENGTH] == '2':
                entry[MEETING_HOUR] = str(int(entry[MEETING_HOUR]) + 1)
                temp_meetings_copy.append(join_date(*entry[:4]))

    new_meet_copy_temp.append(join_date(*new_meet_copy[:4]))
    if new_meet_copy[MEETING_LENGTH] == '2':
        new_meet_copy[MEETING_HOUR] = str(int(new_meet_copy[MEETING_HOUR]) + 1)
        new_meet_copy_temp.append(join_date(*new_meet_copy[:4]))
    for entry in new_meet_copy_temp:
        for meeting in temp_meetings_copy:
            if entry == meeting:
                result = True

    return result


def get_meeting_index(meeting_data, meetings):
    meeting_hour = join_date(*meeting_data[:4])
    index = 0
    for entry in meetings:
        if meeting_hour == join_date(*entry[:4]):
            result = index
        index += 1

    return result


def edit_meeting_data(meeting_data, meetings):
    meeting_index = get_meeting_index(meeting_data, meetings)
    meetings.pop(meeting_index)
    edited_data = get_meeting_data('Enter new data for edited meeting', 'all')
    if validate_if_meeting_overlap(edited_data, meetings):
        ui.print_error('New data for meeging is overlaping existing meeting.')
    else:
        meetings.insert(meeting_index, edited_data)

    return meetings
