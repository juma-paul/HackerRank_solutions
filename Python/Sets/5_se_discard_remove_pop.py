from typing import Set

def sum_set(N: int, s: Set[int]) -> int:
    """
    Print sum of the remaining elements of set s after executing N commands.

    Args:
        N (int): The number of commands to execute on set s.
        s (Set[int]): The set to execute the commands on.

    Returns:
        int: The sum of remaining elements of set s.
    """

    for i in range(N):
        command = input(f'\nCommand {i + 1} of {N}: ').split()
        if command[0] == 'pop':
            s.pop()
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))
    return sum(s)

def main():
    """
    Main function to test functionality of sum_set().
    """

    n = int(input(f'\nHow many elements will be in set s? '))
    s = set(map(int, input(f'\nEnter {n} space-separated integers into set s: ').split()))
    N = int(input(f'\nHow many commands would you like to execute on set s? '))

    res = sum_set(N,s)
    print(res)

if __name__ == '__main__':
    main()