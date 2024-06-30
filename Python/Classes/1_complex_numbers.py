class Complex:
    """
    A class to represent a complex number.
    
    Attributes:
        real (float): The real part of the complex number.
        imaginary (float): The imaginary part of the complex number.
    """

    def __init__(self, real: float, imaginary: float) -> None:
        """
        Initializes the complex number with the given real and imaginary parts.

        Args:
            real (float): The real part of the complex number.
            imaginary (float): The imaginary part of the complex number.
        """

        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, num: 'Complex') -> 'Complex':
        """
        Adds two complex numbers.

        Args:
            num (Complex): The complex number to add.

        Returns:
            Complex: The result of the addition.
        """

        real = self.real + num.real
        imag = self.imaginary + num.imaginary
        return Complex(real, imag)

    def __sub__(self, num: 'Complex') -> 'Complex':
        """
        Subtracts one complex number from another.

        Args:
            num (Complex): The complex number to subtract.

        Returns:
            Complex: The result of the subtraction.
        """

        real = self.real - num.real
        imag = self.imaginary - num.imaginary
        return Complex(real, imag)
    
    def __mul__(self, num: 'Complex') -> 'Complex':
        """
        Multiplies two complex numbers.

        Args:
            num (Complex): The complex number to multiply.

        Returns:
            Complex: The result of the multiplication.
        """

        real = self.real * num.real - self.imaginary * num.imaginary
        imag = self.real * num.imaginary + self.imaginary * num.real
        return Complex(real, imag)
    
    def __truediv__(self, num: 'Complex') -> 'Complex':
        """
        Divides one complex number by another.

        Args:
            num (Complex): The complex number to divide by.

        Returns:
            Complex: The result of the division.
        """

        conjugate = Complex(num.real, -num.imaginary)
        numerator = self * conjugate
        denominator = num.real ** 2 + num.imaginary ** 2
        real = numerator.real / denominator
        imag = numerator.imaginary / denominator
        return Complex(real, imag)
    
    def mod(self) -> 'Complex':
        """
        Returns the modulus of the complex number.

        Returns:
            Complex: The modulus of the complex number.
        """

        real = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        imag = 0
        return Complex(real, imag)
    
    def __str__(self) -> str:
        """
        Returns the string representation of the complex number.

        Returns:
            str: The string representation of the complex number.
        """

        if self.imaginary == 0:
            result = f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            if self.imaginary >= 0:
                result = f"0.00+{self.imaginary:.2f}i"
            else:
                result = f"0.00-{abs(self.imaginary):.2f}i"
        elif self.imaginary > 0:
            result = f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            result = f"{self.real:.2f}-{abs(self.imaginary):.2f}i"
        return result


def main():
    """
    The main function that reads input and performs operations on complex numbers.
    """
    
    c = map(float, input("\nEnter the real and imaginary part of the first complex number separated by a space: ").split())
    d = map(float, input("\nEnter the real and imaginary part of the second complex number separated by a space: ").split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')


if __name__ == '__main__':
    main()
