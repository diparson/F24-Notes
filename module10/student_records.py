from pprint import pprint as pp
import random
# Practice with lists
# Global Constant variables
STUDENT_ID_BASE = 10000
# Global variables
current_student_id = STUDENT_ID_BASE


def generate_student_records(student_records, num_records):
    global current_student_id  # link to global variable
    for i in range(1, num_records + 1):
        current_student_id = current_student_id + 1
        record = {
            'ID': current_student_id,
        }
        student_records.append(record)


# Example usage

def main():
    student_records = []  # initial list of dictionaries
    
    num_records = 5
    generate_student_records(student_records, num_records)
    print(f'Adding {num_records} student records: {student_records}')
    
    num_records = 2
    generate_student_records(student_records, num_records)
    print(f'Adding {num_records} student records: {student_records}')


if __name__ == '__main__':
    # Call main function
    main()
