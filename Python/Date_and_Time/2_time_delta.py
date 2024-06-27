from datetime import datetime

def time_delta(time1: str, time2: str) -> int:
    """
    Calculate the absolute time difference between two timestamps.

    Args:
        time1 (str): The first timestamp in the format 'Day dd Mon yyyy hh:mm:ss +xxxx'.
        time2 (str): The second timestamp in the same format.

    Returns:
        int: The absolute difference between the two timestamps in seconds.
    """

    time_format = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(time1, time_format)
    dt2 = datetime.strptime(time2, time_format)
    delta = abs((dt1 - dt2).total_seconds())
    return int(delta)

def main():
    """
    Main function to accept inputs and test the functionality of the time_delta() function.
    """

    T = int(input('Enter the number of comparisons: '))

    results = []
    for i in range(T):
        time1 = input(f'Enter the {i + 1}-th time (Day dd Mon yyyy hh:mm:ss +xxxx): ').strip()
        time2 = input(f'Enter the {i + 1}-th time (Day dd Mon yyyy hh:mm:ss +xxxx): ').strip()
        delta = time_delta(time1, time2)
        results.append(delta)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
