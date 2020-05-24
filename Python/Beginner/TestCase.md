## DAY 1 TEST CASE
is_perfect_square(9) == True # 3 points <br>
is_perfect_square(100) ==True # 3 points<br>
is_perfect_square(225)==True # 3 points<br>
is_perfect_square(500)==False # 3 points<br>
is_perfect_square.__doc__ != None  # 2 points<br>

## DAY 2 TEST CASE
missing_numbers([1,2,3,4,6,7,10]) ==[5, 8, 9] # 3 points
missing_numbers([10,11,12,14,17])==[13, 15, 16] # 3 points
missing_numbers([2, 3, 5, 1, 6, 4, 12, 8, 20])==[7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19] # 3 points<br>
missing_numbers([2, 6, 10, 4, 11, 15, 19])==[3, 5, 7, 8, 9, 12, 13, 14, 16, 17, 18] # 3 points<br>
missing_numbers.__doc__ != None # 2 points<br>
                                
## DAY3 TEST CASE
even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 18])=='number of even numbers is 6\nnumber of odd numbers is 5' # 4 points<br>
even_odd(range(10, 35))=='number of even numbers is 13\nnumber of odd numbers is 12' # 4 points<br>
even_odd.__doc__ != None # 2 points<br>
even_odd([5, 6, 1, 3, 9])=='number of even numbers is 1\nnumber of odd numbers is 4' # 4 points<br>


## DAY 4 TEST CASE
string_test('The quick Brown Fox')=='Number of Lowercase letters is 13.\nNumber of Uppercase letters is 3.' # 4 points<br>
string_test('My name is Sodiq Agunbiade, I am your tutor for this cohort')=='Number of Lowercase letters is 43.\nNumber of Uppercase letters is 4.' # 4 points<br>
string_test('You are a Student of 30daysofcode'=='Number of Lowercase letters is 24.\nNumber of Uppercase letters is 2.' # 4 points<br>
string_test.__doc__ != None # 2 points<br>

## DAY 5 TEST CASE
unique([1,2,3,3,3,3,4,5])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5]\nUnique List: [1, 2, 3, 4, 5]' # 4 points<br>
unique([1,2,3,3,3,3,4,5,3,3,3,3,4,5,6,6,11,22,33,44])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 3, 3, 3, 3, 4, 5, 6, 6, 11, 22, 33, 44]\nUnique List: [1, 2, 3, 4, 5, 6, 11, 22, 33, 44]' # 4 points<br>
unique([1,2,3,3,3,3,4,5,5,3,3,3,3,4,5,6,6,110,20,19,34])=='Sample List: [1, 2, 3, 3, 3, 3, 4, 5, 5, 3, 3, 3, 3, 4, 5, 6, 6, 110, 20, 19, 34]\nUnique List: [1, 2, 3, 4, 5, 6, 19, 20, 34, 110]' # 4 points<br>
unique.__doc__ != None # 2 points<br>

## DAY 6 TEST CASE


## DAY 7 TEST CASE
averageMultiple(10)==5.75 # 2 points<br>
averageMultiple(100)==50.391304347826086 # 2 points<br>
averageMultiple(124)==62.1578947368421 # 2 points<br>
averageMultiple.__doc__ != None # 2 points<br>
averageMultiple(1234)==617.1443478260869 # 2 points<br>
averageMultiple(90)==45.0# 2 points<br>
averageMultiple(75)==37.5# 2 points<br>
                
## DAY 8 TEST CASE
fastSum>__doc__ != None # 2 points<br>
fastSum(134930284)==9103090837625470 # 3 points<br>
fastSum(12330900)==76025553570450 # 3 points<br>
fastSum(10000000)==50000005000000 # 3 points<br>
fastSum(121344566)==7362251909536461 # 3 points<br>

## DAY 9 TEST CASE

## DAY 10 TEST CASE

## DAY 11 TEST CASE
squareSum(10)==1740 # 3 points<br>
squareSum(-1)=='Wrong Input' # 2 points<br>
squareSum('a')=='Invalid!' # 2 ppoints<br>
squareSum(100)==24174150 # 3 points<br>
squareSum.__doc__ != None # 1 point<br>
squareSum(123))==55682264# 3 points<br>

## DAY 12 TEST CASE

## DAY 13 TEST CASE
k_largest([1, 4, 7, 2, 22, 34, 21, 44, 5, 3], 3)==22 # 3 points<br>
k_largest([3, 555, 2, 11, 444, 12, 24, 42, 244], 5)==24 # 3 points<br>
k_largest([121, 3232, 2323, 43, 2321, 4223, 24232, 222], 3)==3232 # 3 points<br>
k_largest([12, 22, 123, 1, 4, 2, 5, 433, 45, 67], 4)==45 # 3 points<br>
k_largest.__doc__ != None # 1 point<br>
k_largest([1, 2, 3, 4, 5, 6], 1)==6 # 2 points<br>

## DAY 14 TEST CASE
def error(func, num):<br>
    try:<br>
        return func(num)<br>
    except AssertionError: return 1<br>
Triangle_no(12)==False # 2 points<br>
error(Triangle_no, -4)== 1# 2 points<br>
error(Triangle_no, 'a')== 1 # 2 points<br>
Triangle_no(1234)==False # 2 points<br>
Triangle_no(-11)==1 # 2 points<br>
Triangle_no.__doc__ != None # 2 points<br>
Triangle_no(6)==True<br>

## DAY 15 TEST CASE

## DAY 16 TEST CASE

## DAY 17 TEST CASE

## DAY 18 TEST CASE

## DAY 19 TEST CASE

## DAY 20 TEST CASE

## DAY 21 TEST CASE
def error(func, *args):<br>
    try:<br>
        return func(*args)<br>
    except AssertionError: return 1<br>

error(var_sort, ('Jane', 11, 2),  ('Bame', 12, 34), (('Tom', 12, 22)))==[('Bame', 12, 34), ('Jane', 11, 2), ('Tom', 12, 22)] # 2 points<br>
error(var_sort, (1, 1, 1))==1 # 2 points<br>
error(var_sort, ('ade', 11, 2), ('ade', 10, 12), ('ade', 11, 3))==[('ade', 10, 12), ('ade', 11, 2), ('ade', 11, 3)] # 2 points<br>
error(var_sort, ('ade', 2), ('ade', 3, 5)) == 1  # 2 points<br>
error(var_sort, ('ade', 12, 11), ('John', -1, 2))==1 # 2 points<br>
error(var_sort, ('old', 10, 12), ('Old', 10, 12), ('name', 17, 20))==[('Old', 10, 12), ('name', 17, 20), ('old', 10, 12)] # 2 points<br>
error(var_sort, 1) == 1 # 2 points<br>


## DAY 22 TEST CASE
def error(func, manufacturer, model, **mod):<br>
    try:<br>
        return func(manufacturer, model, **mod)<br>
    except AssertionError: return 1<br>
make_car('Toyota', 'Bb188', age=30, color='black', mileage='50miles')=={'manufacturer':'Toyota', 'model': 'Bb188', 'age':30, 'color':'black', 'mileage': '50miles'}) # 2 points<br>
make_car('Camry', 'Ad123', age=150, old=True, owner='Babs')=={'manufacturer':'Camry', 'model':'Ad123', 'age':150, 'old':True, 'owner':'Babs'} # 2 points<br>
error(make_car, 1, 1, new=True)==1 # 3 points<br>
make_car('Honda', '123gdfh', new=False)=={'manufacturer': 'Honda', 'model':'123gdfh', 'new':False} # 2 points<br>
error(make_car,'Buggatti', 1, old=True)==1 # 3 <br>
error(make_car, 123, 'game', is_fast=True)==1 # 3 points<br>
make_car.__doc__ != None # 1 point<br>


## DAY 23 TEST CASE
circle(7).computeArea() =='154cm2'# 3 points<br>
circle(7).computeCircum() =='44cm'# 3 points<br>
circle(7).__doc__!=None # 1 point<br>
circle(7.5).radius ==7.5# 1 point<br>
circle(7.5).computeCircum()=='47cm' #3  points<br>
circle(7.5).computeArea()=='177cm2'# 3 points<br>


## DAY 24 TEST CASE
None

## DAY 25 TEST CASE
Person('Babatunde', 20).name=='Babatunde' # 2 points<br>
Person('Babatunde', 20).addAge(10)=='Babatunde will be 30 in the next 10 years' # 2 points<br>
Person('Babatunde', 20).age==20 # 2 points<br>
Person('Babatunde', 20).printUser()=='Babatunde is 20 years old.' # 2 points<br>
def error(func, val):<br>
    try:<br>
        return func(val)<br>
    except AssertionError: return 1<br>
error(Person('baba', 12).addAge, 'a')==1 # 2 points<br>
error(Person('aba', 2).addAge, -1)==1 # 2 points<br>
error(Person('name', 12).addAge, 12)=='name will be 24 in the next 12 years' # 2 points<br>

## DAY 26 TEST CASE
2*Point(4, 7).__mul__(Point(5, 6))==124 # 2 points<br>
round(Point(1, 4).__add__(Point(4, 6)).__sub__(Point(1, 3)).distance(Point(3, 5)), 5)==2.23607 # 3 points<br>
Point(3, 6).__add__(Point(5, 7)).__mul__(Point(1, 4).__add__(Point(5, 6)))==178 # 2 points<br>
round(Point(-1, 5).distance(Point(6, 4).__mul__(2)), 5)==13.34166 # 2 points<br>
Point(0.5, 7).__mul__(Point(2, 5))==36.0 # 2 points<br>
round((Point(1, 2).__add__(Point(3, 5))).distance(Point(100, 4.6).__sub__(Point(1, 50))), 1)==108.5 # 3 points<br>

## DAY 27 TEST CASE

## DAY 28 TEST CASE

## DAY 29 TEST CASE

## DAY 30 TEST CASE