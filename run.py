import gspread
from google.oauth2.service_account import Credentials

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
    print('Welcome to School Prediciton.')
    print('Enter your name and grades to fins out what college to aplly for.\n')

    student_name = input('Enter your name here (example:John Smith):\n')
    print('Your grades should be entered as so; English, Maths, Science, Option1, Option2, Option3\n')
    student_grades = [input('Please enter your grades here:')]
    print(student_name,student_grades)
def main():
    get_student_grades(data)

main()