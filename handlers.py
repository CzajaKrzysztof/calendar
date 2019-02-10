import ui
import storage
import functions
import os
from datetime import datetime


def program_start(file_name):
    os.system('clear')
    meetings = storage.get_meetings_from_file(file_name)
    today_meeting = functions.get_todays_meetings(meetings)
    ui.show_meetings(today_meeting, 'Your shedule for today', 'yes', True)


def shedule_meeting(file_name):
    meetings = storage.get_meetings_from_file(file_name)
    new_meeting = functions.get_meeting_data('Shedul a new meeting', 'all')
    if functions.validate_if_meeting_overlap(new_meeting, meetings):
        os.system('clear')
        ui.print_error('Meeting is overlaping with another.')
    else:
        meetings.append(new_meeting)
        storage.write_table_to_file(file_name, meetings)
        os.system('clear')
        ui.show_meetings([new_meeting], 'Meeting added', 'no')


def edit_meeting(file_name):
    meetings = storage.get_meetings_from_file(file_name)
    ui.show_meetings(meetings, 'All your meetings')
    meeting_data = functions.get_meeting_data('Enter date of meeting to edit', 'edit')
    if functions.validate_meeting(meeting_data, meetings):
        meetings = functions.edit_meeting_data(meeting_data, meetings)
        storage.write_table_to_file(file_name, meetings)
        meetings = storage.get_meetings_from_file(file_name)
        today_meetings = functions.get_todays_meetings(meetings)
        os.system('clear')
        ui.show_meetings(today_meetings, 'Your shedule for today', 'yes', True)
    else:
        os.system('clear')
        ui.print_error('No meeting on that date')


def cancel_meeting(file_name):
    meetings = storage.get_meetings_from_file(file_name)
    os.system('clear')
    today_meeting = functions.get_todays_meetings(meetings)
    ui.show_meetings(today_meeting, 'Your shedule for today', 'yes')
    meeting_to_delete = [datetime.now().year, datetime.now().month, datetime.now().day]
    meeting_to_delete.append(functions.get_meeting_data('Enter date of meeting to cancel', 'cancel')[0])
    print(meeting_to_delete)
    if functions.validate_meeting(meeting_to_delete, meetings):
        meetings = functions.cancel(meeting_to_delete, meetings)
        storage.write_table_to_file(file_name, meetings)
        meetings = storage.get_meetings_from_file(file_name)
        today_meetings = functions.get_todays_meetings(meetings)
        os.system('clear')
        ui.show_meetings(today_meetings, 'Compacted meetings for today', 'yes', True)
    else:
        os.system('clear')
        ui.print_error('No entry for that date.')


def compact_meetings(file_name):
    meetings = storage.get_meetings_from_file(file_name)
    current_date = functions.get_currnet_date()
    today_meetings = functions.get_todays_meetings(meetings)
    functions.compact(today_meetings)
    storage.write_table_to_file(file_name, meetings)
    meetings = storage.get_meetings_from_file(file_name)
    today_meetings = functions.get_todays_meetings(meetings)
    os.system('clear')
    ui.show_meetings(today_meetings, 'Compacted meetings for today', 'yes', True)
