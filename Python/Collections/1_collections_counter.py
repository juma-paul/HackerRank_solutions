from collections import Counter
from typing import List

def calculate_earnings(shoe_sizes: List[int], customer_requests: List[tuple]) -> int:
    """
    Calculate the total earnings from selling shoes to customers based on availability and demand.

    Args:
        shoe_sizes (List[int]): The available shoe sizes.
        customer_requests (List[tuple]): A list of tuples reprsenting shoe size and the price.

    Returns:
        int: The total earnings from the sales.
    """

    inventory = Counter(shoe_sizes)
    total_earnings = 0

    for size, price in customer_requests:
        if inventory[size] > 0:
            total_earnings += price
            inventory[size] -= 1

    return total_earnings

def main():
    """
    Main function to handle input and output for the shoe sales program.
    """

    X = int(input('\nHow many pairs of shoes are available? '))
    shoe_sizes = list(map(int, input('\nEnter space-separated shoe sizes: ').split()))

    if len(shoe_sizes) != X:
        print(f'\nShoe sizes must be {X}, but you entered {len(shoe_sizes)}')
        return
    
    N = int(input('\nHow many customers are interested in buying the shoes? '))

    customer_requests = []
    for i in range(N):
        size, price = map(int, input(f'\nEnter shoe size and price separated by space {i + 1} of {N}: ').split())
        customer_requests.append((size, price))

    total_earnings = calculate_earnings(shoe_sizes, customer_requests)
    print(f'\nThe shoe shop owner earned {total_earnings}\n')

if __name__ == '__main__':
    main()
