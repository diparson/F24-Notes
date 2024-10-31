import string

# Read CSV file with student information

ID = 0
FIRST_NAME = 1
LAST_NAME = 2
EMAIL = 3
GENDER = 4
SSN = 5


def read_data(file_name):
    """Open CSV file with data and returns it as a list

    Args:
        file_name (str): CSV file name

    Returns:
        lst: Data from file
    """
    data = []
    with open(file_name, mode='rt', encoding='utf-8') as in_file:
        for rec in in_file:
            # Remove extra '\n' character
            # print(f'record [{rec.strip()}]')
            data.append(rec.strip())

    return data


def female_records(data):
    """Create a file with records whose records are gender = 'Female'
    Args: data (lst): Data of csv records
    """
    # 1) Open file for writing using 'with'
    file_name = 'female_records.csv'
    with open(file_name, mode='wt', encoding='utf-8') as out_file:
        print(f'Writing to file {file_name}')
        # Loop over all records and save only those
        for rec in data:
            # 2) Write the header
            if rec.startswith('id'):
                out_file.write(rec + '\n')
            else:
                parts = rec.split(',')
                # Save only records with Female as gender
                if parts[GENDER] == 'Female':
                    out_file.write(rec + '\n')
                else:
                    continue


def last_name_ends_with(data, lname_ends):
    file_name = f'last_name_ends_{lname_ends}.csv'
    with open(file_name, mode='wt', encoding='utf-8') as out_file:
        print(f'Writing to file {file_name}')
        for rec in data:
            if rec.startswith('id'):
                out_file.write(rec + '\n')
            else:
                parts = rec.split(',')
                if parts[LAST_NAME].endswith(lname_ends):
                    out_file.write(rec + '\n')
                else:
                    continue


def wsu_email_builder(data):
    """Generate WSU email for each student, 
        and overwrite the current one and save the rest
        Format:<first_name><last_name><last_4_ssn>@mail.weber.edu
        All lower case
        Ex: 2,Lani,Baukham,lbaukham1@bandcamp.com,Female,869-11-2698
            2,Lani,Baukham,lanibaukham2698@mail.weber.edu,Female,869-11-2698

    Args:
        data (lst): CSV records
    """
    file_name = f'students_wsu_data.csv'
    with open(file_name, mode='wt', encoding='utf-8') as out_file:
        print(f'Writing to file {file_name}')
        for rec in data:
            if rec.startswith('id'):
                out_file.write(rec + '\n')
            else:
                parts = rec.split(',')
                # 1) Build new email
                wsu_email = parts[FIRST_NAME].lower() + parts[LAST_NAME].lower() + parts[SSN][-4:] + '@mail.weber.edu'
                # 2) Overwrite the email field
                # print(f'Original email[{parts[EMAIL]}], new email[{wsu_email}]')
                parts[EMAIL] = wsu_email
                # 3) Write the record to the file
                separator = ','
                out_file.write(separator.join(parts) + '\n')


def main():
    # Assumes the file is at the root directory
    data_file = 'MOCK_DATA.csv'
    data = read_data(data_file)
    print(f'Data file has {len(data)} records')
    # Task 1: Create a file with records whose gender = 'Female'
    female_records(data)
    # Task 2: Create a file with records whose last name ends with:
    lname_ends = 'ton'
    last_name_ends_with(data, lname_ends)
    lname_ends = 'w'
    last_name_ends_with(data, lname_ends)
    # Task 3: Generate new emails
    wsu_email_builder(data)


if __name__ == '__main__':
    # Call main function
    main()
