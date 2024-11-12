# Practice list comprehensions
import timeit


def test_regular_list(numbers):
    # Task 1: Create a list of squares of numbers
    squares = []
    for rec in numbers:
        if rec % 2 == 1:
            squares.append(rec * rec)
    print(f'Numbers: {numbers}')
    print(f'Squares: {squares}')


def test_list_comprehension(numbers):
    # Use a list comprehension to create a list of squares of numbers
    squares = [rec * rec for rec in numbers]
    print(f'Squares: {squares}')


def test_list_comprehension_conditional(numbers):
    # Use a list comprehension to create a list of squares of numbers
    squares = [rec * rec for rec in numbers if rec % 2 == 1]
    print(f'Squares: {squares}')


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_regular_list(numbers)

    test_list_comprehension_conditional(numbers)


if __name__ == '__main__':
    # Call main function
    main()
