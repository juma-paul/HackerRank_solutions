def main():
    """
    Receive inputs, do integer divisiona and appropriately handle exceptions that may occur.
    """

    N = int(input(f'\nEnter the number of pairs: '))

    results = []

    for _ in range(N):
        a, b = input(f'\nEnter a pair of space-separated values: ').split()
        try:
            div = int(a) // int(b)
            results.append(div)
        except ZeroDivisionError as zde:
            results.append(f'Error Code: {zde}')
        except ValueError as ve:
            results.append(f'Error Code: {ve}')
    
    for result in results:
        print(f'\n{result}\n')


if __name__ == '__main__':
    main()