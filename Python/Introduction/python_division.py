def main():
    """
    Main function to execute the program.
    """

    while True:
        try:
            a = int(input('\nEnter the first integer: '))
            b = int(input('\nEnter the second integer: '))
            if b == 0:
                raise ZeroDivisionError('cannot divide by zero.')
        except ValueError:
            print('Invalid input, please enter a valid integer.')
        except ZeroDivisionError as e:
            print(f'ZeroDivisionError: {e}')
        else:
            print(f'\nInteger division = {a // b}\nFloat division = {a / b}')
            break
            

if __name__ == '__main__':
    main()