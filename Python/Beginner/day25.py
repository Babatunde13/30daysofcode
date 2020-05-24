class Person:
    '''A person object'''
    def __init__(self, name, age):
        self.name = name
        self.age=age

    def addAge(self, n):
        '''Increments the age by n'''
        assert type(n)==int and n > 0, 'Invalid Input'
        return f'{self.name} will be {self.age+n} in the next {n} years'

    def printUser(self):
        return f'{self.name} is {self.age} years old.'
    
Person('Babatunde', 20).__dict__=={'name': 'Babatunde', 'age': 20} # 2 points
Person('Babatunde', 20).addAge(10)=='Babatunde will be 30 in the next 10 years' # 2 points
Person('Babatunde', 20).age==20 # 2 points
Person('Babatunde', 20).printUser()=='Babatunde is 20 years old.' # 2 points
def error(func, val):
    try:
        return func(val)
    except AssertionError: return 1
error(Person('baba', 12).addAge, 'a')==1 # 2 points
error(Person('aba', 2).addAge, -1)==1 # 2 points
error(Person('name', 12).addAge, 12)=='name will be 24 in the next 12 years' # 2 points