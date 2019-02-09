import handlers
import ui


def main():
    file_name = 'meetings.txt'
    handlers.program_start(file_name)
    choice = ui.default_view()
    while choice != 'q':
        if choice == 's':
            handlers.shedule_meeting(file_name)
            choice = ui.default_view()
        elif choice == 'c':
            handlers.remove_meeting(file_name)
            choice = ui.default_view()


if __name__ == "__main__":
    main()
