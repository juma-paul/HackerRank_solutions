from itertools import combinations_with_replacement

def print_combinations_with_replacement(S: str, k: int) -> None:
    """
    Prints all possible size k combinations of the characters in string S 
    with replacement, sorted in lexicographic order.
    
    Args:
        S (str): The input string from which combinations are generated.
        k (int): The size of each combination.
    
    Returns:
        None
    """
    
    combs_with_replacement = combinations_with_replacement(sorted(S), k)

    for item in combs_with_replacement:
        print(''.join(item))
    

def main():
    """
    Reads user input, processes it, and prints size k combinations with replacement.
    """

    try:
        user_input = input("Enter a string S and an integer k separated by space: ").strip()
        S, k = user_input.split()
        S = S.upper()
        k = int(k)
        
        print_combinations_with_replacement(S, k)
    except ValueError:
        print("Invalid input. Please enter a string and an integer separated by space.")

if __name__ == "__main__":
    main()
