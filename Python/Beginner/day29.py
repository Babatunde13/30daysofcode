class Person:
    def __init__(self, name, age):
        assert type(name)==str and type(age)==int and age>0, 'Invalid'
        self.name = name
        self.age = age
    
    def getGender(self):
        return 'Human'
    
    def age_n(self, n):
        return self.age + n

class Male(Person):
    def getGender(self):
        return 'male'

class Female(Person):
    def getGender(self):
        return 'female'

def error(func, *val):
    try: return func(*val)
    except AssertionError: return 1

Person('Babatunde', 2).getGender()=='Human' # 2 points
Male('Babatunde', 20).age_n(30)==30 # 2 points
Female('Sayo', 30).age_n(30)==60 # 2 points
Male('Ade', 40).getGender()=='male' # 2 points
error(Male, 'Ba', -2)==1 # 3 points
error(Female, True, 10)==1 # 3 points