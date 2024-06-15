def main():
    """
    Main function for executing the logic for arithmetic operators problem
    """

    while True:
        try:
            a = int(input("\nEnter the first integer: "))
            b = int(input("\nEnter the second integer: "))
        except ValueError:
            print(f"Invalid input, please enter a valid integer.")
        else:
            print(f'Sum = {a + b}\nDifference = {a - b}\nProduct = { a * b}')
            break

if __name__ == '__main__':
    main()
