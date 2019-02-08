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
        ui.show_meetings(today_meeting, 'Todays meetings', 'yes')
        ui.print_main_menu()
        choice = ui.get_menu_choice()
        if choice == 's':
            print('Choice is s')
        elif choice == 'c':
            print('Choice is c')


if __name__ == "__main__":
    main()
