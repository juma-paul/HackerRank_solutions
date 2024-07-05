import textwrap

def wrap(string: str, max_width: int) -> str:
    """
    Wraps the input string into lines of specified maximum width.

    Args:
        string (str): The input string to be wrapped.
        max_width (int): The maximum width of each line.

    Returns:
        str: The wrapped string with lines separated by newline characters.
    """

    wrapped_text = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped_text)

def main():
    """
    Main function to execute the wrapping of input string based on user input for maximum width.
    """
    
    string = input('\nEnter string: ')
    max_width = int(input('\nEnter maximum length to wrap: '))
    res = wrap(string, max_width)
    print(f'\n{res}\n')

if __name__ == '__main__':
    main()
