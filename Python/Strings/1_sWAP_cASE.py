def swap_case(s: str) -> str:
    """
    Swap cases of a string from uppercase to lowercase and vice versa.

    Args:
        s (str): The string to swap the cases.

    Returns:
        str: The string with swapped cases.
    """

    result = []
    for char in s:
        if char.isupper():
            result.append(char.lower())
        else:
            result.append(char.upper())
    return ''.join(result)

def main():
    """
    Main method to execute logic for the swap case function.
    """

    s = input("\nEnter the string to swap cases (e.g., 'wWW.hACKERrANK.COM'): ")
    result = swap_case(s)
    print(f'\n{s} with cases swaped to {result}\n')

if __name__ == '__main__':
    main()