class Complex:
    '''Complex number object'''
    def __init__(self, real, imaginary):
        '''Constructor'''
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        '''String representation'''
        return f'Complex({self.real}, {self.imaginary})'

    def __add__(self, other):
        '''Addition of complex numbers'''
        return Complex(self.real+other.real, self.imaginary+other.imaginary)

    def __sub__(self, other):
        '''Subtraction of complex numbers'''
        return Complex(self.real-other.real, self.imaginary-other.imaginary)

    def __mul__(self, other):
        '''Multiplication of complex numbers'''
        real = self.real*other.real + self.imaginary*other.imaginary*-1
        imag = self.imaginary*other.real + self.real*other.imaginary
        return Complex(real, imag)

    def conjugate(self):
        return Complex(self.real, -self.imaginary)
    
    def __div__(self, other):
        '''Division of complex numbers'''
        num = Complex(self.real, self.imaginary).__mul__(Complex(other.real,  other.imaginary).conjugate())
        den = other.real**2-other.imaginary**2                                                                                                
        return Complex(round(num.real/den, 2), round(num.imaginary/den, 2))



Complex(-2, 4).__add__(Complex(3, 4)).__dict__=={'real': 1, 'imaginary': 8} # 3 points
Complex(1, 8).__sub__(Complex(-2, 4)).__dict__=={'real': 3, 'imaginary': 4} # 3 points
Complex(1, 3).__mul__(Complex(2, 4)).__dict__=={'real': -10, 'imaginary': 10} # 3 points
Complex(1, 3).__div__(Complex(2, 4)).__dict__=={'real': -1.17, 'imaginary': -0.17} #3 points
Complex(3+1-2+6, 6+4).__dict__=={'real': 8, 'imaginary': 10} # 2 points