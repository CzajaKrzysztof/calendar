import ui
import storage
import functions
import os
from datetime import datetime


def main():
    file_name = 'shedul.csv'
    choice = 'x'
    while choice != 'q':
        os.system('clear')
        meetings = storage.get_meetings_from_file(file_name)
        today_meeting = functions.get_todays_meetings(meetings)
        ui.show_meetings(today_meeting, 'Your shedule for today', 'yes')
        ui.print_main_menu()
        choice = ui.get_menu_choice()
        if choice == 's':
            meetings = storage.get_meetings_from_file(file_name)
            new_meeting = functions.get_meeting_data()
            meetings.append(new_meeting)
            storage.write_table_to_file(file_name, meetings)
            os.system('clear')
            ui.show_meetings([new_meeting], 'Meeting added', 'no')
            ui.print_main_menu()
            choice = ui.get_menu_choice()
        elif choice == 'c':
            pass


if __name__ == "__main__":
    main()
