from itertools import permutations

def main():
    """
    Create k possible  permutations of a given string S.
    """

    S, k = input("Eneter space-separated string number of permutations needed: ").split()
    S = S.upper()
    k = int(k)

    permut_S = permutations(sorted(S), k)

    for item in permut_S:
        item = "".join(item)
        print(item)

if __name__ == "__main__":
    main()