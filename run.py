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
        print('Enter your name and grades to find out what college to apply for.\n')
        student_name = input('Enter your name here (example:John Smith):\n')
        print('Your grades should be entered as so; English, Maths, Science, Option1, Option2, Option3\n')
        student_grades_inp = input('Please enter your grades here:')
        student_grades = student_grades_inp.split(',')
        student_info = [student_name,student_grades]
        
        if validate_name(student_info) and validate_grades(student_info) and check_for_duplicate(student_info):
            print('data is valid\n')
            break
        elif validate_name(student_info) and validate_grades(student_info) and (check_for_duplicate(student_info) is not True):
            print('Data has already been entered\n')
    return (student_info)

def validate_name(data):
    """
    Check the name entered to make sure that only etters and spaces are entered
    """
    name = data[0]
    if all(letter.isalpha() or letter.isspace() for letter in name):
        return True
    else:
        print(f'{name} is invalid, must only contain letters\n')
        return False

def validate_grades(data):
    """
    Check the list contains 6 items.
    """
    grades = data[1]
    if len(grades) == 6:
        print('Grades are valid\n')
        return True
    else:
        print('Grades are invlaid, please enter 6 letters seperated by commas\n')

def update_worksheet(data, worksheet):
    """
    Update the given worksheet with the data in the correct format
    """
    student_info = [data[0].title()]
    for x in data[1]:
        student_info.append(x.capitalize())
    print(f'Updating {worksheet.capitalize()} worksheet...\n')
    spec_worksheet = SHEET.worksheet(worksheet)
    spec_worksheet.append_row(student_info)
    print(f'{worksheet.capitalize()} worksheet updated successfully.\n')

def check_for_duplicate(data):
    """
    Check the database to see if their name has already been entered to avoid duplicates.
    """
    name = data[0].title()
    all_names = SHEET.worksheet('grades').col_values(1)
    if name in all_names:
        print(f'{name} has already been entered\n')
        return False
    else:
        print('name has not been entered\n')
        return True
def main():
    student = get_student_grades(data)
    update_worksheet(student, 'grades')
main()