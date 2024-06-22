def main():
    """
    Reads two integers and prints their integer division, remainder, and divmod result.
    """

    a = int(input("Enter integer a: "))
    b = int(input("Enter integer b: "))
    quotient, remainder = divmod(a, b)
    
    print(f"\n{quotient}\n{remainder}\n{(quotient, remainder)}")

if __name__ == '__main__':
    main()
