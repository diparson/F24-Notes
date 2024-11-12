"""
Test use of model for aircraft flights
"""
from airtravel import Flight


def main():
    print(Flight)
    f1 = Flight('SN060') # use parentheses to call the constructor
    print(f'Flight type {f1}')
    print(f'Flight number {f1.number()}')
    f2 = Flight('DL123') # use parentheses to call the constructor
    print(f'Flight number {f2.number()}')


if __name__ == '__main__':
    # Call main function
    main()
