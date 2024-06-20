def main():
    '''
    Print symmetric difference between two sets in ascending order.
    '''

    M = int(input('\nHow many elements for set M: '))
    a = set(map(int, input(f'\nEnter {M} space-separated elements for set M: ').split()))
    if len(a) != M:
        print(f"Error: Expected {M} elements, but got {len(a)}.")
        return

    N = int(input('\nHow many elements for set N: '))
    b = set(map(int, input(f'\nEnter {N} space-separated elements for set N: ').split()))
    if len(b) != N:
        print(f"Error: Expected {N} elements, but got {len(b)}.")
        return

    a_dif = a.difference(b)
    b_dif = b.difference(a)

    res = sorted(a_dif.union(b_dif))
    
    print("\nSymmetric difference in ascending order: ")
    for i in res:
        print(i)

if __name__ == '__main__':
    main()
