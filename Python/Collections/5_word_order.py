from collections import OrderedDict, Counter

def main():
    """
    Read words from input, count their occurrences using Counter,
    and print the count of unique words followed by their occurrences.
    """

    n = int(input('\nHow many words? '))

    words = []
    for _ in range(n):
        word = input(f'\nEnter word {_ + 1}: ')
        words.append(word)

    count = Counter(words)

    word_dict = OrderedDict()
    for word in words:
        if word not in word_dict:
            word_dict[word] = count[word]

    print(len(word_dict))

    for cnt in word_dict.values():
        print(cnt, end=' ')
    print()
    
if __name__ == '__main__':
    main()
    

