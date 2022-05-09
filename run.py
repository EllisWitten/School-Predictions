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
        student_grades_inp = input('Please enter your grades here:')
        student_grades = student_grades_inp.split(',')
        student_info = [student_name,student_grades]
        
        if validate_name(student_info) and validate_grades(student_info):
            print('Data is valid')
            break
    return (student_info)

def validate_name(data):
    """
    Check the name entered to make sure that only etters and spaces are entered
    """
    name = data[0]
    print(f'this is your name:{name}')
    if all(letter.isalpha() or letter.isspace() for letter in name):
        print(f'{name} is a valid name')
        return True
    else:
        print(f'{name} is invalid, must only contain letters')
        return False

def validate_grades(data):
    """
    Check the list contains 6 items.
    """
    grades = data[1]
    if len(grades) == 6:
        print('Grades are valid')
        return True
    else:
        print('Grades are invlaid, please enter 6 letters seperated by commas')

def update_worksheet(data, worksheet):
    student_info = [data[0].capitalize()]
    for x in data[1]:
        student_info.append(x.capitalize())
    print(student_info)
    print(f'Updating {worksheet.capitalize()} worksheet...\n')
    spec_worksheet = SHEET.worksheet(worksheet)
    spec_worksheet.append_row(student_info)
    print(f'{worksheet.capitalize()} worksheet updated successfully.\n')

def main():
    student = get_student_grades(data)
    update_worksheet(student, 'grades')
main()