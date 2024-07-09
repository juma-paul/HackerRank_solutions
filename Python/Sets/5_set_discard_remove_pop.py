from typing import Set

def sum_set(num_commands: int, set_s: Set[int]) -> int:
    """
    Print sum of the remaining elements of set_s after executing num_commands.

    Args:
        num_commands (int): The number of commands to execute on set_s.
        set_s (Set[int]): The set to execute the commands on.

    Returns:
        int: The sum of remaining elements of set_s.
    """

    for i in range(num_commands):
        command = input(f'\nCommand {i + 1} of {num_commands}: ').split()
        if command[0] == 'pop':
            set_s.pop()
        elif command[0] == 'remove':
            set_s.remove(int(command[1]))
        elif command[0] == 'discard':
            set_s.discard(int(command[1]))
    return sum(set_s)

def main():
    """
    Main function to test functionality of sum_set().
    """

    num_elements = int(input(f'\nHow many elements will be in set s? '))
    set_s = set(map(int, input(f'\nEnter {num_elements} space-separated integers into the set_s: ').split()))
    num_commands = int(input(f'\nHow many commands would you like to execute on set_s? '))

    result = sum_set(num_commands, set_s)
    print(result)

if __name__ == '__main__':
    main()
