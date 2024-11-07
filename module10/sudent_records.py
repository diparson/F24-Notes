from pprint import pprint as pp
import random
# Practice with lists
# Global Constant variables
STUDENT_ID_BASE = 10000
# Global variables
current_student_id = STUDENT_ID_BASE


def set_students_id(student_records, number):
    global current_student_id  # link to global variable
    for _ in range(number):
        current_student_id = current_student_id + 1
        record = {'student_id': current_student_id}
        student_records.append(record)



def main():
    student_records = []  # initial list of dictionaries

    student_number = 5
    set_students_id(student_records, student_number)
    print(f'1) Students: {student_records}')


if __name__ == '__main__':
    # Call main function
    main()
