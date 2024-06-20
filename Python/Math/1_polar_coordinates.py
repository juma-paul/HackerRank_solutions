import cmath

def polar_coordinates(complex_num: complex) -> str:
    """
    Return the polar cordinates of a given complex number.

    Args:
        complex_num (complex): The complex number to return polar coordinates for.

    Returns:
        str: Modulus and phase of the complex number (polar coordinates).
    """
    modulus = abs(complex_num)
    phase = cmath.phase(complex_num)

    return f'\n{modulus}\n{phase}'

def main():
    """
    Main function to test functionality of polar_coordinates().
    """

    complex_num = input(f'\nEnter a complex number (no space between elements): ')
    try:
        complex_num = complex(complex_num)
        polar_coordinate = polar_coordinates(complex_num)
        print(polar_coordinate)
    except ValueError as e:
        print(f'ValueError: {e}')

if __name__ == '__main__':
    main()