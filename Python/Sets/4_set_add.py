from typing import List

def country_stamp(stamps: List[str]) -> int:
    """
    Find the total number of distinct country stamps.

    Args:
        stamps (List[int]): The list of country stamps.
    
    Returns:
        int: The total number of distinct country stamps.
    """

    distinct_stamps = set(stamps)
    
    return len(distinct_stamps)

def main():
    """
    Main function to accept input and test country_stamp()
    """

    n = int(input('\nHow many country stamps do you want to enter? '))
    stamps = []
    for i in range(n):
        stamp = input(f'\nEnter country stamp {i + 1}: ')
        stamps.append(stamp)

    res = country_stamp(stamp)
    print(f'\nThere are {res} distinct country stamps')

if __name__ == '__main__':
    main()

