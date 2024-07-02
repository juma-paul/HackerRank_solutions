from typing import List

def char_type(s: str) -> List[bool]:
    """
    Checks whether the input string 's' contains any alphanumeric characters, 
    alphabetical characters, digits, lowercase characters, and uppercase characters.

    Args:
        s (str): The input string to check.

    Returns:
        list (bool): A list of booleans in the order of [has_alnum, has_alpha, has_digit, has_lower, has_upper].
    """

    has_alnum = has_alpha = has_digit = has_lower = has_upper = False
    
    for char in s:
        if not has_alnum and char.isalnum():
            has_alnum = True
        if not has_alpha and char.isalpha():
            has_alpha = True
        if not has_digit and char.isdigit():
            has_digit = True
        if not has_lower and char.islower():
            has_lower = True
        if not has_upper and char.isupper():
            has_upper = True
    
        # Exit loop if all conditions are already met
        if has_alnum and has_alpha and has_digit and has_lower and has_upper:
            break
    
    return [has_alnum, has_alpha, has_digit, has_lower, has_upper]

def main():
    """
    Main function to read input from the user and call the `char_type` function.
    """

    s = input('\nPlease enter a string: ')
    results = char_type(s)
    for result in results:
        print(f'\n{result}\n')

if __name__ == '__main__':
    main()
