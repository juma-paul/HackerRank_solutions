def main():
    """
    Reads three numbers (a, b, and m) from input, computes a^b, and (a^b) % m if m is non-negative and others integers.
    """

    try:
        a = float(input("\nEnter a number a: "))
        b = float(input("\nEnter a number b: "))
        m = int(input("\nEnter a non-negative number b: "))

        if m < 0:
            raise ValueError("\nm must be a non-negative integer.")

    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f'TypeError: {e}')
    else:
        power_mod = pow(int(a), int(b), m)
        power = pow(a, b)
        print(f'\nPower: {power:,.4f}\nMod Power: {power_mod:,.4f}')

if __name__ == "__main__":
    main()