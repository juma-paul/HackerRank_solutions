def print_full_name(first: str, last: str) -> str:
    """
    Return first and last name in a message.

    Args:
        first (str): The first name.
        last (str): The last name.

    Returns:
        str: The string message containing the first and last names.
    """

    return f'Hello {first} {last}! You just delved into python.'

def main():
    """
    Main function to test functionality of print_full_name().
    """

    first_name = input('\nWhat is your first name? ')
    last_name = input('\nWhat is your last name? ')

    msg = print_full_name(first_name, last_name)
    print(f'\n{msg}\n')

if __name__ == '__main__':
    main()