def runner_up(n, arr):
    """
    Determining runner up for the results of a sports day.

    Args:
        n (int): Number of scores.
        arr (int): List of scores.

    Returns:
        int: the runner-up score.
    """

    winner = max(arr)
    list_minus_winner = [i for i in arr if i != winner]
    runner_up = max(list_minus_winner)
    
    return runner_up


def main():
    '''
    Main function to execute logic of runner_up()
    '''

    n = int(input("\nEnter the number of scores: "))
    arr = list(map(int, input("\nEnter the elements separated by space: ").split())) # prompt for array, split by space, map to integers

    res = runner_up(n, arr)
    print(res)

if __name__ == '__main__':
    main()