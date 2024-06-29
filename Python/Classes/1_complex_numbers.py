class Complex:
    def __init__(self, real: float, imaginary: complex) -> None:
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, num: 'Complex') -> 'Complex':
        real = self.real + num.real
        imag = self.imaginary + num.imaginary
        return Complex(real, imag)

    
    def __sub__(self, num: 'Complex') -> 'Complex':
        real = self.real - num.real
        imag = self.imaginary - num.imaginary
        return Complex(real, imag)
    
    def __mul__(self, num: 'Complex') -> 'Complex':
        real = self.real * num.real - self.imaginary * num.imaginary
        imag = self.real * num.imaginary + self.imaginary * num.real
        return Complex(real, imag)
    
    def __truediv__(self, num: 'Complex') -> 'Complex':
        conjugate = Complex(num.real, -num.imaginary)
        numerator = self * conjugate
        denomenator = num.real ** 2 + num.imaginary ** 2
        real = numerator.real / denomenator
        imag = numerator.imaginary / denomenator
        return Complex(real, imag)
    
    def mod(self) -> complex:
        real = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        imag = 0
        return Complex(real, imag)
    
    def __str__(self) -> str:
        pass

def main():
    pass

if __name__ == '__main__':
    main()