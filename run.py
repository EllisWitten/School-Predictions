import gspread
from google.oauth2.service_account import Credentials
import string

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('CREDS.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('school_predictions')

spreadsheet = SHEET.worksheet('grades')
data = spreadsheet.get_all_values()

def get_student_grades(data):
    """
    Get student name and grades
    """
    while True:
        print('Welcome to School Prediciton.')
        print('Enter your name and grades to find out what college to aplly for.\n')
        student_name = input('Enter your name here (example:John Smith):\n')
        print('Your grades should be entered as so; English, Maths, Science, Option1, Option2, Option3\n')
        student_grades = [input('Please enter your grades here:')]
        student_info = [student_name,student_grades]
        
        if validate_name(student_info) and validate_grades(student_info):
            print('Data is valid')
            break

def validate_name(data):
    """
    Check the name entered to make sure that only etters and spaces are entered
    """
    name = data[0]
    if name.isalpha() == True:
        print(f'{name} is a vlaid name')
        return True
    else:
        print(f'{name} is invalid, must only contain letters')
        return False

def validate_grades(data):
    """
    Check the grades to make sure only letters between A and F have been entered.
    Check the list contains 6 items
    """
    grades = data[1]
    return True


def main():
    student = get_student_grades(data)

main()