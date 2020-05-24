def make_car(man, model, **car):
    '''
    A function that takes two argument of type string and arbitrary arguments and returns a distionary.
    '''
    assert type(man)==type(model)==str, 'Input must be a string'
    return {'manufacturer': man, 'model': model, **car}
print(make_car('Toyota', 'Bb188', age=30, color='black', mileage='50miles')=={'manufacturer':'Toyota', 'model': 'Bb188', 'age':30, 'color':'black', 'mileage': '50miles'}) # 2 points

def error(func, manufacturer, model, **mod):
    try:
        return func(manufacturer, model, **mod)
    except AssertionError:
        return 1
make_car('Toyota', 'Bb188', age=30, color='black', mileage='50miles')=={'manufacturer':'Toyota', 'model': 'Bb188', 'age':30, 'color':'black', 'mileage': '50miles'}) # 2 points
make_car('Camry', 'Ad123', age=150, old=True, owner='Babs')=={'manufacturer':'Camry', 'model':'Ad123', 'age':150, 'old':True, 'owner':'Babs'} # 2 points
error(make_car, 1, 1, new=True)==1 # 3 points
make_car('Honda', '123gdfh', new=False)=={'manufacturer': 'Honda', 'model':'123gdfh', 'new':False} # 2 points
error(make_car,'Buggatti', 1, old=True)==1 # 3 points
error(make_car, 123, 'game', is_fast=True)==1 # 3 points
make_car.__doc__ != None # 1 point
