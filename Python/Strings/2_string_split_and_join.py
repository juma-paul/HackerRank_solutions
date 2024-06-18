def string_split_and_join(line: str) -> str:
    """
    Split a space-separated string and join the words with a hyphen(-).

    Args:
        line (str): The space-separated string.

    Returns:
        str: The hyphen(-) separated string.
    """

    line = line.split()
    result = '-'.join(line)
    return result

def main():
    """
     Main function to execute string_split_and_join().
    """

    line = input("\nEnter a space-separated string to split and join with '-': ")
    result = string_split_and_join(line)
    print(f'\n{line} ----> {result}\n') 

if __name__ == '__main__':
    main()