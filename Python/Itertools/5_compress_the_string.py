from itertools import groupby

def compress_string(S: str) -> None:
    """
    Compress the string by replacing consecutive occurrences of characters
    with the character and its count.
    
    Args:
        S (str): The input string consisting of digits.
    
    Returns:
        None
    """
    
    result = []
    for key, char in groupby(S):
        count = len(list(char))
        result.append(f'({count}, {key})')
    
    for item in result:
        print(item, end=' ')

def main():
    """
    Main function to read user input and compress the string of digits.
    """

    try:
        S = input('Enter a string of digits (0-9): ').strip()
        compress_string(S)
    except ValueError as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
