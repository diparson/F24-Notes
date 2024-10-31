# Practice Simple Exceptions
import sys


def convert(s):
    """Convert to integer

    Args:
        s (str, realNumber): object to convert

    Returns:
        int: integer of input
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f'\tConversion failed [{str(e)}]', sys.stderr)

    return -1


# Starting Point
# Program "Driver"
def main():
    # print(int('34'))          # GOOD: string of all numberic values
    # print(int(1.5))           # GOOD: float
    # print(int('1.5'))         # BAD: ValueError
    # print(int([1.5, 2.4]))    # BAD: TypeError
    # print(int('34'))          # GOOD: string of all numberic values

    print(convert('34'))          # GOOD: string of all numberic values
    print(convert('hello'))       # BAD: string of all numberic values
    print(convert([1, 2, 3]))

    print('Done')


if __name__ == '__main__':
    # Call main function
    main()
