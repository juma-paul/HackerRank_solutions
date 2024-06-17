def list_cmds(num, arr):
    """
    Read python list commands in a specific format to perform tasks.

    Args:
        num (int): Number of commands to enter.
        arr (list): A list containing the command and possible arguments.

    Returns:
        None: The function does not return anything.
    """

    for _ in range(num):
        cmd = input().split()
        if cmd[0] == 'insert':
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(arr)
        elif cmd[0] == 'remove':
            arr.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            arr.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            arr.sort()
        elif cmd[0] == 'pop':
            arr.pop()
        elif cmd[0] == 'reverse':
            arr.reverse()

def main():
    """
    Main method to execute the commands as written in list_cmds().
    """
    
    n = int(input("Num of cmd: "))
    lst = []
    list_cmds(n, lst)

if __name__ == '__main__':
    main()
