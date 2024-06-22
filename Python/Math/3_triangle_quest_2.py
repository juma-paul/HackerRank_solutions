def main():
    """
    Generates and prints a palindromic triangle of a given size.
    """
    for i in range(1, int(input("Enter integer to represent size of triangle: ")) + 1):
        print((10 ** i // 9) ** 2)

if __name__ == '__main__':
    main()
