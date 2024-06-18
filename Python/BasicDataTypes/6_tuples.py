def main():
    """
    Main function to calculate the hash value of a tuple.

    Reads an integer n and n space-separated integers as input, creates a tuple from them,
    and calculates and prints the hash value of the tuple.
    """
    
    n = int(input("How many elements do you want in your tuple? "))
    if n <= 0:
        print("Number of elements must be a positive integer.")
        return

    items = input("Enter space-separated integers: ").split()[:n]
    tuple_t = tuple(map(int, items))
    tuple_hash = hash(tuple_t)
    print("Hash value of the tuple:", tuple_hash)

if __name__ == '__main__':
    main()
