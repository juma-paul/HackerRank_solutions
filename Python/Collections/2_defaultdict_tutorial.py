from collections import defaultdict
from typing import List

def word_indices(group_A: List[str], group_B: List[str]) -> None:
    """
    Prints the indices of each word in group_B as they appear in group_A.
    If a word in group_B does not appear in group_A, print -1.

    Args:
        group_A (List[str]): List of words in group A.
        group_B (List[str]): List of words in group B.
    
    Returns:
        None
    """

    indices = defaultdict(list)

    for index, word in enumerate(group_A):
        indices[word].append(index + 1)

    for word in group_B:
        if word in indices:
            print(' '.join(map(str, indices[word])))
        else:
            print(-1)

def main():
    """
    Reads input values for groups A and B, and calls word_indices to process and print the results.
    """

    m, n = map(int, input('\nEnter n (size of group A words) and m (size of group B words) separated by space: ').split())

    group_A = [input(f'\nEnter word {i + 1} for group A: ').strip() for i in range(m)]

    group_B = [input(f'\nEnter word {i + 1} for group B: ').strip() for i in range(n)]

    word_indices(group_A, group_B)

if __name__ == '__main__':
    main()
