from itertools import combinations

def main():
    """
    Generates and prints all possible combinations of the characters in a string 'S' of length up to 'k' in lexicographically sorted order.
    """
    
    try:
        S, k = input("Enter a string S and an integer k separated by space: ").split()
        S = S.upper()
        k = int(k)

        comb_S = []
        for r in range(1, k+1):
            comb_S += list(combinations(sorted(S), r))

        for i in comb_S:
            print("".join(i))
    
    except ValueError:
        print("Invalid input. Please enter a string and an integer separated by space.")

if __name__ == "__main__":
    main()
