import handlers


def main():
    file_name = 'meetings.txt'
    choice = handlers.program_start(file_name)
    while choice != 'q':
        if choice == 's':
            choice = handlers.shedule_meeting(file_name)
        elif choice == 'c':
            choice = handlers.remove_meeting(file_name)


if __name__ == "__main__":
    main()
