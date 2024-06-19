def mutate_strings(string: str, pos: int, char: str) -> str:
    """
    Mutate a string by modifying a character in a given position.

    Args:
        string (str): The string to modify.
        pos (int): The position of the character to modify.
        char (str): The character to modify with.
    
    Returns:
        str: The modified string
    """

    new_str = string[:pos] + char + string[pos + 1:]
    return new_str

def main():
    """
    Main function to test functionality of mutate_strings().
    """

    try:
        s = input('\nEnter string: ')
        position, character = input('\nEnter position (1-based index) and new character separated by a space: ').split()

        position = int(position) - 1 # Convert to 0-based index

        new_string = mutate_strings(s, position, character) 
        print(f"\n{new_string}\n")
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'An unexpected error occured: {e}')

if __name__ == '__main__':
    main()