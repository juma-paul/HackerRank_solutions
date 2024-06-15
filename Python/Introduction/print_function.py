def main():
    """
    Main function to execute the print function problem
    """

    while True:
        try:
            n = int(input("\nEnter an integer value: "))
        except ValueError as e:
            print(f'\nValueError: {e}')
        else:
            if 1 <= n <= 150:
                for i in range(n):
                    print(i + 1, end="")
                print()
                break
            else:
                print("\nEnter an integer between 1 and 150 inclusive. Try again")

if __name__ == '__main__':
    main()