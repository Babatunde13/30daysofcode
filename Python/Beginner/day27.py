class Shape:
    def __init__(self, lenght):
        assert type(lenght)==float or type(lenght)==int and lenght > 0, 'Invalid'
        self.lenght = lenght
    
    def area(self):
        return 0
    
    def shape(self):
        return 'I am a shape.'
    
class Square(Shape):
    def area(self):
        return self.lenght ** 2

def error(func, val):
    try: return func(val)
    except AssertionError: return 1

error(Square, '7')==1 # 3 points
error(Square, -1)==1 # 3 points
Square(7).area(), Square(7).shape()=='49 I am a shape.' # 3 points
error(Shape, 'a')==1 # 3 points
Square(7).__dict__ == {'lenght': 7} # 2 points