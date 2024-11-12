"""
Test use of model for aircraft flights
"""
from airtravel import Flight


def main():
    print(Flight)
    f1 = Flight('SN060') # use parentheses to call the constructor
    print(f'F1 Flight type {f1}')
    print(f'F1 Flight number {f1.number()}')
    
    f2 = Flight('DL123') # use parentheses to call the constructor
    print(f'F2 Flight number {f2.number()}')
    f2.set_number('DL456')
    print(f'F2 Flight number {f2.number()}')
    
    # f3 = Flight('DL12344') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    # f3 = Flight('9L123') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    # f3 = Flight('dl123') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    # f3 = Flight('DL1A3') # use parentheses to call the constructor
    # print(f'Flight number {f3.number()}')
    f3 = Flight('DL193') # use parentheses to call the constructor
    print(f'F3 Flight number {f3.number()}')


if __name__ == '__main__':
    # Call main function
    main()
