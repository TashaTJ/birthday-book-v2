# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread 
import pyfiglet
import pyfiglet.fonts
import colorama
import pkg_resources
import os
from colorama import Fore, Back, Style
from google.oauth2.service_account import Credentials 
from pyfiglet import figlet_format
import pyinputplus as pyip
colorama.init(autoreset=True)



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('birthday_book_v2')
BIRTHDAY_WORKSHEET = SHEET.worksheet('birthdays')


def user_response(message, min_value, max_value):
    """
    Function validates users input from a list of choices.
    used throughout the programme
    """
    input = pyip.inputInt(prompt=message, min=min_value, max=max_value)
    return input


def main_menu_():
    """
    User selects a numbered option, 
    function uses their input and runs
    elif loop to trigger the next process.
    If user inputs invalid choice, programme 
    will continue to ask for a valid input.
    """
    print(
        "\n 1. Search Birthdays\n 2. Add a new Birthday\n\
 3. Edit Exisiting Birthday\n 4. Retrieve all Birthdays\n")
    while True:
        user_input = user_response(Fore.BLACK + Back.WHITE + 
            "\nPlease enter a number from the above options: ", 1, 4
            )
        if user_input == 1:
            search_birthday()
            break
        elif user_input == 2:
            add_new_birthday()
            break
        elif user_input == 3:
            edit_birthday_from_menu()
            break
        else:
            retrieve_all_birthdays()
            break
        return False


def another_task():
    """
    Function returns user to the main menu if they'd 
    like to perform another action
    """
    print(Fore.BLACK + Back.WHITE + "\nWould you like to perform another action?\n")
    print("1. Yes, back to main menu\n\
2. No, I'm done")
    while True:
        user_input = user_response(Fore.BLACK + Back.WHITE + 
            "\nPlease enter a number from the above options: ", 1, 2
            )
        if user_input == 1:
            print(Fore.BLACK + Back.WHITE + "\nReturning to the main menu...\n")
            main_menu_()
            break
        else:
            print(Fore.CYAN +
                "Exiting programme...\n")
            raise SystemExit


def retrieve_records():
    """
    Function to retrieve all records found
    in the birthday book spreadhseet.
    """
    return BIRTHDAY_WORKSHEET.get_all_records(numericise_ignore=['all'])

def findCell(info_type, search_by):
    result = list(filter(
        lambda record: record[info_type] == search_by or
        search_by in record[info_type], retrieve_records()
        ))
    return result


def retrieve_all_birthdays():
    """
    Function to retrieve full list of Birthday entries
    from google worksheet
    """
    all_birthdays = retrieve_records()
    print(Fore.BLACK + Back.WHITE + "\nNow retrieving all Birthdays...\n")
    for birthday in all_birthdays:
        print_records_in_loop(birthday)
    
    another_task()


def print_records(records, function=None):
    """
    Function to print a single birthday contact.
    To be used in the birthday search functions.
    """
    print(Fore.BLACK + Back.WHITE + "\nNow printing your birthdays(s)...\n")
    for record in records:
        print_records_in_loop(record)


def print_records_in_loop(record):
    """
    Function to loop through all records passed
    as a parameter and print the details in a
    list of key: values.
    """
    for key, value in record.items():
        if key == 'phone_number':
            # Ensures 0 is added to the front of the number
            value1 = str(value).zfill(11)
            print(f"{key}: {value1}")
        else:
            print(Fore.CYAN + f"{key}: {value}")
    print("\n")


def run_programme():
    """
    This function calls on all other functions
    to run the programme
    """
    print(pyfiglet.figlet_format('BIRTHDAY  BOOK \
\n', font='smslant', justify="center"))
    print(Back.CYAN + '\nInstructions:\n\
- From the menu, type a number and then press enter.\n\
- For a Y or N choice, please type Y or N and press enter.\n\
- To restart the programme, press the "Run Programme" at the top.')
    print(Fore.BLACK + Back.WHITE + '\nmain menu...\n')
    main_menu_()

run_programme()