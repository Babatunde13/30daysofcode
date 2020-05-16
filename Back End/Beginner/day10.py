def isPerfect(num):
  '''
  A function which checks if a number is a perfect square without using the power operator and any built-in function.
  Parameter: num, int
  Returns: True if num is a perfect square, False if otherwise.

  @author: Babatunde Koiki
  Created on: 10-05-2020
  '''  
  n = 1
  while n * n<= num: 
        
      # If (i * i = n) 
      if num % n == 0 and num / n == n: 
          return True
            
      n = n + 1
  return False

