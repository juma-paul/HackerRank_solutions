from typing import List

def average(arr: List[int]) -> float:
    """
    Compute the average of distinct elements in an array.

    Args:
        arr (List[int]): The integer aray whose average needs to be computed.

    Returns:
        float: The average value of an array rounded to 3 decimal places.
    """

    arr = set(arr) 
    result = sum(arr) / len(arr)
    return result

def main():
    """
    Main function to test functionality of average().
    """

    n = int(input("\nEnter size of the array: "))

    while True:
        arr = list(map(int, input(f"\nEnter {n} space-separated integers: ").split()))
        if len(arr) == n:
            break
        else:
            print(f'\nThe array size should be {n}. You entered {len(arr)} elements.')

    avg = average(arr)
    print(f'\nAverage of all plants with distinct heights: {avg:.3f}\n')

if __name__ == '__main__':
    main()