def main():
    """
    Main function to execute the loops
    """
    
    MAX_ATTEMPTS = 3
    for _ in range(MAX_ATTEMPTS):
        try:
            n = int(input('\nEnter an integer: '))
            if n < 0:
                print('\nPLease enter a positive integer.')
                continue
        except ValueError as e:
            print(f'ValueError: {e}')
        else:
            for i in range(0, n):
                print(i ** 2)
            break
    else:
        print('You have reached the maximum attempts. Exiting the program.')

if __name__ == '__main__':
    main()