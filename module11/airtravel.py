"""
Model for aircraft flights
"""


class Flight:
    # Define initializer method or constructor
    # This is called when an object is created
    def __init__(self, number):
        # Define instance variables
        self._number = number
    
    # Functions inside classes are called methods
    # This is also called a "getter" method
    # First parameter MUST be 'self' is a reference to 
    # the object that is being created
    def number(self):
        return self._number

    # This is also called a "setter" method
    def set_number(self, number):
        self._number = number   


def main():
    pass


if __name__ == '__main__':
    # Call main function
    main()
