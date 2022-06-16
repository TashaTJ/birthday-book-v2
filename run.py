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


def run_programme():
    print(pyfiglet.figlet_format('BIRTHDAY  BOOK \
\n', font='smslant', justify="center"))
    print(Back.CYAN + '\nInstructions:\n\
- From the menu, type a number and then press enter.\n\
- For a Y or N choice, please type Y or N and press enter.\n\
- To restart the programme, press the "Run Programme" at the top.')
    print(Fore.BLACK + Back.WHITE + '\nmain menu...\n')
    main_menu_()

run_programme()