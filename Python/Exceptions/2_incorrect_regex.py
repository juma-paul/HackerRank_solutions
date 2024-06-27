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