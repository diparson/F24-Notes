"""
Model for aircraft flights
"""


class Flight:
    # Define initializer method or constructor
    # This is called when an object is created
    def __init__(self, number):
        #If any of the rules below fall, raise ValueError
        #Must be 5 characters long
        if len(number) != 5:
            raise ValueError(f' Invalid flight number length [{number}]')
        #First two characters (Airline Code) should be alpha
        if not number[:2],isalpha():
            raise ValueError(f' Invalid airline code [{number[:2]}]')
        #First two characters should be uppercase
        if not number[:2].supper()
           raise ValueError(f' Invalid airline code [{number[:2]}]')
        #last three characters ( Airline Flight number) 
         if not number[:2].isdigit():
           raise ValueError(f' Invalid airline code [{number[:2]}]')  
             return number[:2]
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
