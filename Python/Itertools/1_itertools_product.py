from itertools import product

def main():
    """
    Accepts two iterables A and B as inputs and calculates their cartesian product, returning them as tuples separated by space.
    """
    
    try:
        A = list(map(int, input("\nEnter the space-separated values for iterable A: ").split()))
        B = list(map(int, input("\nEnter the space-separated values for iterable B: ").split()))

        cart_product = list(product(A, B))

        for item in cart_product:
            print(item, end=" ")
        print()
    
    except ValueError as e:
        print(f"ValueError: {e}")

if __name__ == "__main__":
    main()
