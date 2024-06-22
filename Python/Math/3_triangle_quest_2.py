def main():
    """
    Generates and prints a palindromic triangle of a given size.
    """

    n = int(input("Enter integer to represent size of triangle: "))
    for i in range(1, n + 1):
        k = (10 ** i // 9) # create a number composed entirely of 1s
        print(k ** 2) # create a palindromic number

if __name__ == '__main__':
    main()
