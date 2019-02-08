import ui
import storage
import os


def main():
    os.system('clear')
    ui.print_main_menu()
    choice = ui.get_menu_choice()
    print(choice)


if __name__ == "__main__":
    main()
