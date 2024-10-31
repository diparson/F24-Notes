# Module to calculate sqrt of a number


def sqrt(x):
    """ Compute the square root using the method
    of Heron of Alexandria

    Args:
        x (int): Integer to compute the sqrt

    Returns:
        float: Square root of input

    Raise Error: ValueError on division by zero
    """

    if x < 0:
        raise ValueError(f'\tCannot compute sqrt of [{x}]')

    # Good to go
    guess = x
    i = 0  # 20 iterations
    while guess*guess != x and i < 20:
        guess = (guess + x/guess)/2.0

    return guess

# Starting Point
# Program "Driver"


def main():
    try:
        print(sqrt(9))
        print(sqrt(11))
        number = -1
        print(sqrt(number))
    except ValueError:
        print('Bad input')

    print('Done!!!')


if __name__ == '__main__':
    # Call main function
    main()
