from pprint import pprint as pp
import random
# Practice with lists
# Global Constant variables
STUDENT_ID_BASE = 10000
# Global variables
current_student_id = STUDENT_ID_BASE


def set_students_id(student_records, num_records):
    global current_student_id  # link to global variable
    for i in range(1, num_records + 1):
        current_student_id = current_student_id + 1
        record = {
            'ID': current_student_id,
        }
        student_records.append(record)


def set_students_quizzes(student_records, num_quizzes):
    # Student records is a list of dictionaries
    for record in student_records:
        # check if key 'quizzes' exists
        if 'quizzes' not in record:
            record['quizzes'] = []   # create key 'quizzes' with empty list
        for i in range(1, num_quizzes + 1):
            record['quizzes'].append(random.randint(0, 100))


def calculate_quiz_average(student_records):
    for record in student_records:
        if 'quizzes' in record:
            quiz_total = sum(record['quizzes'])
            quiz_average = quiz_total / len(record['quizzes'])
            record['quiz_average'] = quiz_average
        else:
            record['quiz_average'] = 0


def display_student_records(student_records):
    for record in student_records:
        print(f"ID: {record['ID']}")
        if 'quizzes' in record:
            print(f"Quizzes: {record['quizzes']}")
        print(f"Quiz Average: {record['quiz_average']}")
        print()


def main():
    student_records = []  # initial list of dictionaries

    num_records = 5
    set_students_id(student_records, num_records)
    print(f'Adding {num_records} student records: {student_records}')

    num_records = 2
    set_students_id(student_records, num_records)
    print(f'\nAdding {num_records} student records: {student_records}')

    num_quizzes = 3
    set_students_quizzes(student_records, num_quizzes)
    pp(f'\nSetting {num_quizzes} quizzes for each student: {student_records}')

    num_quizzes = 1
    set_students_quizzes(student_records, num_quizzes)
    pp(f'\nSetting {num_quizzes} quizzes for each student: {student_records}')

    calculate_quiz_average(student_records)
    print('\nCalculating quiz average for each student:')
    display_student_records(student_records)


if __name__ == '__main__':
    # Call main function
    main()
