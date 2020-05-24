def BCalculator(bin1: str, bin2: str) -> int:
  '''
  A function that takes two binary numbers and return their sum u=in decimal

  Parameters: -------------
            bin1: str, first binary number
            bin2: str, second binary number

  Returns: ---------------
          the sum of bin1 and bin2 in decimal

  @author: Babatunde Koiki
  Created on: 08-05-2020
  '''
  def bintodec(num):
    n, dec = len(num)-1, 0
    for _ in num: 
      dec += int(_)* (2 ** n)
      n -=1
    return dec
  return bintodec(bin1)+bintodec(bin2)


      
