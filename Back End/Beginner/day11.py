def hcf(n1, n2):
  '''
  A function that returns the highest common factor between two numbers.
  parameters: n1 and n2, the two numbers
  Returns: the gcd of n1 and n2

  @author: Babatunde Koiki
  Created on: 11-05-2020
  '''
  
  res = 0 #Creates a dummy variable
  for i in range(1, min([n1, n2])): # Loops from 1 to the smaller value
     if n1%i==n2%i==0: res = i # Changes the value of res if there's a common factor
    
  return res
