def main():
    """
    Reads two integers from input and prints:
        - The integer division of the first integer by the second.
        - The remainder of the first integer divided by the second.
        - The result of divmod on the two integers as a tuple.
    """

    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    quotient, remainder = divmod(a, b)
    print(quotient)
    print(remainder)
    print((quotient, remainder))

if __name__ == '__main__':
    main()
