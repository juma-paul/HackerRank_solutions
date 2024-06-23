from itertools import combinations_with_replacement

def print_combinations_with_replacement(s, r):
    """
    Generates and prints all possible combinations of the characters in a string 's' of length 'r' with replacement 
    in lexicographically sorted order.
    """
    # Generate combinations with replacement
    combinations = combinations_with_replacement(s, r)
    
    # Print each combination
    for combo in combinations:
        print(''.join(combo))

if __name__ == "__main__":
    try:
        # Read input
        user_input = input("Enter a string S and an integer k separated by space: ").strip()
        s, r = user_input.split()
        r = int(r)
        
        # Ensure the string is sorted
        s = ''.join(sorted(s))
        
        # Print combinations
        print_combinations_with_replacement(s, r)
    
    except ValueError:
        print("Invalid input. Please enter a string and an integer separated by space.")
