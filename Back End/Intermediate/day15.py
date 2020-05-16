def pascalTriangle(num: int) -> str: 
  '''
  A function that returns the pascal triangle from 1 to num
  '''
  a = '' # Initialises the empty string where all list are
  for line in range(0, num) : 
      # Every line has number of integers equal to line number 
    c = [binomial(line, i) for i in range(0, line + 1)]
    a += f'{c}\n'
  return a
  

def binomial(num: int, k: int) -> int : 
    res = 1
    if (k > num - k) : 
        k = num - k 
    for i in range(0 , k) : 
        res = res * (num - i) 
        res = res // (i + 1) 
      
    return res 
