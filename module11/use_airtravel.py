"""
Test use of model for aircraft flights
"""
from airtravel import Flight


def main():
    print(Flight)
    f = Flight() # use parentheses to call the constructor
    print(f)


if __name__ == '__main__':
    # Call main function
    main()
