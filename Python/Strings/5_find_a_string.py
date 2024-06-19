def count_substring(string: str, sub_string: str) -> int:
    """
    Count number of times a substring occur in a given string.

    Args:
        string (str): The string with which we compare the substring.
        sub_string (str): The substring to count the number of occurance.

    Returns:
        int: The number of times substring occurs in string.
    """
    count = 0
    for j in range(len(string) - len(sub_string) + 1):
        if string[j:j + len(sub_string)] == sub_string:
            count += 1

    return count


def main():
    """
    Main Function to test functionality of count_substring.
    """

    string = input("\nEnter the string: ")
    sub_string = input("\nEnter the sub-string: ")

    count = count_substring(string, sub_string)
    print(count)

if __name__ == '__main__':
    main()