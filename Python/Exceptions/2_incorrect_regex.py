import re

def is_valid_regex(pattern: str) -> bool:
    """
    Function to check if the given regex pattern is valid.
    
    Args:
        pattern (str): The regex pattern to check.
    
    Returns:
        bool: True if the pattern is valid, False otherwise.
    """

    invalid_patterns = [r'\*\+', r'\+\*', r'\+\+', r'\?\+', r'\+\?', r'\?\?']
    for invalid_pattern in invalid_patterns:
        if re.search(invalid_pattern, pattern):
            return False
        
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False

def main():
    """
    Main function to read input and print whether each regex pattern is valid or not.
    """
    
    T = int(input('\nHow many test cases would you like to enter? '))
    
    res = []
    for test in range(T):
        S = input(f'Enter test case {test + 1}: ')
        res.append(is_valid_regex(S))
    
    for items in res:
        print(f'\n{items}')

if __name__ == "__main__":
    main()