import string

# Read CSV file with student information


def read_data(file_name):
    """Open CSV file with data and returns it as a list

    Args:
        file_name (str): CSV file name

    Returns:
        lst: Data from file
    """
    data = []
    with open(file_name) as in_file:
        for rec in in_file:
            # Remove extra '\n' character
            # print(f'record [{rec.strip()}]')
            data.append(rec.strip())

    return data


def first_name_analysis(data, initial):
    """Count number of first names that begin
       with a given initial 

    Args:
        data (lst): data list
        initial (str): Initial to filter data by

    Returns:
        int: number of matches
    """
    total = 0
    for row in data:  # Loop over rows
        columns = row.split(',')  # use a comma to split record
        # print(columns[1])  # Index 1 is first_name
        # slice the str to take only first char
        if initial == columns[1][0:1]:
            total += 1
        # for colum in columns: # Loop over columns
        #     print(colum)

    return total


def first_name_analysis_all(data):
    total = 0
    results = {}  # store letter and total
    ascii_letters = string.ascii_uppercase  # get all ASCII values uppercase
    for letter in ascii_letters:
        total = first_name_analysis(data, letter)
        print(f'For {letter}, {total} records')
        results[letter] = total

    return results


def print_first_name_stats(totals):
    # Print Highest Occurrence
    letter = max(totals, key=totals.get)  # get highest value key
    print(f'Highest letter is {letter} with total of {totals[letter]}')
    # Print Lowest Occurrence
    letter = min(totals, key=totals.get)  # get highest value key
    print(f'Lowest letter is {letter} with total of {totals[letter]}')


def gender_analysis_all(data):
    """Run statistics for the gender column (4 col) 

    Args:
        data (lst): Data records

    Returns:
        dict: Gender as the key, and total as the value

    Note: For NUll entries, use 'na'
    """
    results = {}
    for row in data[1:]:  # loop over row, excluding header
        columns = row.split(',')
        if columns[4] == '':  # empty
            key = 'NA'
        else:
            key = columns[4]

        if key in results:    # populate dict
            results[key] += 1
        else:
            results[key] = 1
    return results


def female_records(data):
    # Open file for writing
    # First records SHOULD be the header
    # Make sure you close the file
    pass

# Starting Point
# Program "Driver"


def main():
    # Assumes the file is at the root directory
    data_file = 'MOCK_DATA.csv'
    data = read_data(data_file)
    print(f'Data file has {len(data)} records')
    # Task 1: Create a file with records whose gender = 'Female'


if __name__ == '__main__':
    # Call main function
    main()
