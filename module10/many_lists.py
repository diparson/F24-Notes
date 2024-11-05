from pprint import pprint as pp
import random
# Practice with lists
# Global Constant variables
STUDENT_ID_BASE = 10000
# Global variables
current_student_id = STUDENT_ID_BASE


def add_students(students, number):
    global current_student_id  # link to global variable
    # Create a list with the numbers 0 to number
    # Student IDs wil begin with the number #Student ID
    for _ in range(number):
        current_student_id = current_student_id + 1
        students.append(current_student_id)

    return students


def add_student_id(student_id):
    student_info = {}  # student info, 'id'
    student_info['id'] = student_id  # add student ID to dictionary
    return student_info


def add_quiz_scores(student_info, scores):
    for number in range(1, scores + 1):
        # TODO: Need to find a way to get the last quiz number key
        # and go from there.  This will allow for multiple quizzes
        quiz_id = f'quiz{number}'
        # Random quiz scores as values between 50 and 100 based on scores input
        student_info[quiz_id] = random.randint(50, 100)


def build_student_info(students, scores):
    student_records = []  # return list
    # Create a dictionary with student 'id' as the key and
    # IDs from students as values
    for student_id in students:
        student_info = add_student_id(student_id)  # returns dictionary
        add_quiz_scores(student_info, scores)  # returns nothing
        student_records.append(student_info)  # add dictionary to list
    return student_records


def main():
    student_number = 5
    students = []  # initial list
    students = add_students(students, student_number)
    print(f'1) Students: {students}')
    student_number = 3
    students = add_students(students, student_number)
    print(f'2) Students: {students}')
    quiz_number = 3
    student_grades = build_student_info(students, quiz_number)
    pp(f'3) Student Grades: {student_grades}')
    # quiz_number = 1
    # student_grades = build_student_info(students, quiz_number)
    # pp(f'4) Student Grades: {student_grades}')


if __name__ == '__main__':
    # Call main function
    main()
