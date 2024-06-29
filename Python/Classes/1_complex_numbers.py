class Complex:
    def __init__(self, real: float, imaginary: complex) -> None:
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, num: float) -> complex:
        ...
    
    def __sub__(self, num: float) -> complex:
        ...
    
    def __mul__(self, num: float) -> complex:
        ...
    
    def __truediv__(self, num: float) -> complex:
        ...
    
    def __str__(self) -> str:
        ...
    
    def mod(self) -> complex:
        ...

def main():
    ...

if __name__ == '__main__':
    main()