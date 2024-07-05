import textwrap

def wrap(string: str, max_width: int) -> str:
    wrapped_text = textwrap.wrap(string, max_width)
    return '\n'.join(wrapped_text)

def main():
    string, max_width = input('\nEnter string: '), int(input('\nEnter maximum length to wrap: '))
    res = wrap(string, max_width)
    print(f'\n{res}\n')

if __name__ == '__main__':
    main()