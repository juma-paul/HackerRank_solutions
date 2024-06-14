def is_weird(n):
    if n % 2 != 0:
        return True
    elif 2 <= n <= 5:
        return False
    elif 6 <= n <= 20:
        return True
    else:
        return False

def get_input():
    return int(input('\nPlease enter an integer: '))


def main():
    n = get_input()
    if is_weird(n):
        print('Weird')
    else:
        print('Not Weird')

if __name__ == '__main__':
    main()