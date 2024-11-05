# Practice with lists
# Global Constant variables
STUDENT_ID_BASE = 10000
# Global variables
current_student_id = STUDENT_ID_BASE

def add_students(students, number):
    global current_student_id # link to global variable
    # Create a list with the numbers 0 to number
    # Student IDs wil begin with the number #Student ID
    for _ in range(number):
        current_student_id = current_student_id + 1
        students.append(current_student_id)
    
    return students

# Starting Point
# Program "Driver"
def main():
    student_number = 5
    students = [] # initial list
    students =add_students(students, student_number)
    print(f'1) Students: {students}')
    student_number = 3
    students =add_students(students, student_number)
    print(f'2) Students: {students}')


if __name__ == '__main__':
    # Call main function
    main()
