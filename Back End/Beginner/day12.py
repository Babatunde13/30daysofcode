def quad(a: int, b: int, c: int) -> tuple:
  '''
  A funcion that takes in the terms in a quadratic equation and returns it's roots.
  Parameter: --------
            a: int, coefficient of x^2
            b: int, coefficient of x
            c: int, constant term
  
  @author: Babatunde Koiki
  Created on: 12-05-2020
  '''
  num1, num2, den = -1*b + (b**2-4*a*c)**0.5, -1*b - (b**2-4*a*c)**0.5, 2*a
  return num1/den, num2/den
  