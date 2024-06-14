def is_weird(n):
    """
    Determines if a number is classified as Weird and Not Weird.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if it is Weird, False otherwise.
    """
    
    if n % 2 != 0:
        return True
    elif 2 <= n <= 5:
        return False
    elif 6 <= n <= 20:
        return True
    else:
        return False

def get_input():
    """
    Prompts the user to to enter an integer.

    Returns:
        int: The integer entered by the user.
    """

    return int(input('\nPlease enter an integer: '))


def main():
    """
    Main function to text the program logic.
    """

    n = get_input()
    if is_weird(n):
        print('Weird')
    else:
        print('Not Weird')

if __name__ == '__main__':
    main()