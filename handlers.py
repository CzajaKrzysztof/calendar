import ui
import storage
import functions
import os


def program_start(file_name):
    os.system('clear')
    meetings = storage.get_meetings_from_file(file_name)
    today_meeting = functions.get_todays_meetings(meetings)
    ui.show_meetings(today_meeting, 'Your shedule for today', 'yes')
    ui.print_main_menu()
    choice = ui.get_menu_choice()

    return choice


def shedule_meeting(file_name):
    meetings = storage.get_meetings_from_file(file_name)
    new_meeting = functions.get_meeting_data()
    if functions.validate_if_meeting_overlap(new_meeting, meetings):
        os.system('clear')
        ui.print_error('Meeting is overlaping with another.')
    else:
        meetings.append(new_meeting)
        storage.write_table_to_file(file_name, meetings)
        os.system('clear')
        ui.show_meetings([new_meeting], 'Meeting added', 'no')
    ui.print_main_menu()
    choice = ui.get_menu_choice()

    return choice


def remove_meeting(file_name):
    meetings = storage.get_meetings_from_file(file_name)
    meeting_to_delete = functions.get_meeting_data(False)
    if functions.validate_meeting_to_delete(meeting_to_delete, meetings):
        meetings = functions.remove(meeting_to_delete, meetings)
        storage.write_table_to_file(file_name, meetings)
    else:
        ui.print_error('No entry for that date.')
    ui.print_main_menu()
    choice = ui.get_menu_choice()

    return choice
