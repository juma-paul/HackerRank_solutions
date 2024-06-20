from typing import List, Set

def no_idea(arr: List[int], set_A: Set[int], set_B: Set[int]) -> int:
    """
    Calculate happiness based on the presence of integers in set_A and set_B in arr.

    Args:
        arr (List[int]): The array of integers.
        set_A (Set[int]): The set of integers you like.
        set_B (Set[int]): The set of integers you dislike.

    Returns:
        int: The final happiness score.
    """

    happiness = 0
    for i in arr:
        if i in set_A:
            happiness += 1
        elif i in set_B:
            happiness -= 1
    return happiness

def main():
    """
    Main function to read input, validate input lengths, and calculate happiness.
    """

    n, m = map(int, input(f'\nEnter 2 space-separated integers for length of array and sets respectively: ').split())
    n_arr = list(map(int, input(f'\nEnter {n} space-separated integers: ').split()))
    if len(n_arr) != n:
        print(f'\nYou entered {len(n_arr)} elements instead of {n}.')
        return

    set_A = set(map(int, input(f'\nEnter {m} space-separated integers for set A: ').split()))
    if len(set_A) != m:
        print(f'\nYou entered {len(set_A)} elements instead of {m}.')
        return

    set_B = set(map(int, input(f'\nEnter {m} space-separated integers for set B: ').split()))
    if len(set_B) != m:
        print(f'\nYou entered {len(set_B)} elements instead of {m}.')
        return
    
    result = no_idea(n_arr, set_A, set_B)
    print(result)

if __name__ == '__main__':
    main()
