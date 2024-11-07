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


def set_student_quizzes(student_records, number_quizzes):
    for record in student_records:  # loop over a list of dictionaries
        # Check if the key 'quizzes' exists in the dictionary
        if 'quizzes' not in record:
            record['quizzes'] = []  # create empty list
        # Add random quiz scores to the list
        for _ in range(number_quizzes):
            record['quizzes'].append(random.randint(50, 100))


def calculate_quiz_average(student_records):
    # Create a new key 'quiz_average' in each dictionary
    for record in student_records:
        if 'quizzes' in record:
            quiz_total = sum(record['quizzes'])
            total_quizzes = len(record['quizzes'])
            record['quiz_average'] = quiz_total / total_quizzes
        else:
            record['quiz_average'] = 0


def display_student_records(student_records):
    print('Student Records:')
    for record in student_records:
        print(f"\nStudent ID: {record['student_id']}")
        if 'quizzes' in record:
            print(f"Quizzes: {record['quizzes']}")
            print(f"Quiz Average: {record['quiz_average']}")


def main():
    student_records = []  # initial list of dictionaries

    student_number = 5
    set_students_id(student_records, student_number)
    print(f'1) Students: {student_records}')

    student_number = 1
    set_students_id(student_records, student_number)
    print(f'\n2) Students: {student_records}')

    number_quizzes = 3
    set_student_quizzes(student_records, number_quizzes)
    print(f'\n3) Students: {student_records}')

    number_quizzes = 1
    set_student_quizzes(student_records, number_quizzes)
    print(f'\n4) Students: {student_records}')

    calculate_quiz_average(student_records)
    print(f'\n5) Students: {student_records}')

    display_student_records(student_records)

    # Display second record
    print(f'\nSecond Record: {student_records[1]}')
    # Display second record, third quiz score
    print(f"\nSecond Record: {student_records[1]['quizzes'][2]}")


if __name__ == '__main__':
    # Call main function
    main()
