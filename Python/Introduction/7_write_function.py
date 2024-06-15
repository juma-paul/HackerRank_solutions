def leap_year(year: int) -> bool:
    """
    Determine if a given year is a leap year.

    Args:
        year (int): The year that need to be determined.

    Returns:
        bool: True if it is a leap year, False otherwise.
    """

    # A year is a leap year if it satisfies the following conditions:
    # - The year is divisible by 4, AND
    # - The year is NOT divisible by 100, UNLESS
    # - The year is also divisible by 400.

    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False



def main():
    """
    Main function to execute the logic of leap_year()
    """

    year = int(input('\nPlease enter the year'))
    res = leap_year(year)
    print(res)

if __name__ == '__main__':
    main()