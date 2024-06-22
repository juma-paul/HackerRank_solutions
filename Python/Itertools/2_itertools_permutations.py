from itertools import permutations

def main():
    """
    Create k possible  permutations of a given string S.
    """

    S, k = input("Enter a string S and an integer k separated by space: ").split()
    S = S.upper()
    k = int(k)

    permut_S = permutations(sorted(S), k)

    for item in permut_S:
        item = "".join(item)
        print(item)

if __name__ == "__main__":
    main()