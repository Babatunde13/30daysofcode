def myPackaging(numOfDigits: int, num: int) -> str:
  '''
  A function named myPackaging which right shifts a number. It adds zeros to the front of the number. The number of zeros to add is the value of first argument - second argument

  Parameters: ----------
            numOfDigits: int, the required size of the number
            num: int, the number to change it's size

  Returns: --------------
          A string containing numbers. 

  @author: Babatunde Koiki
  Created on: 03-05-2020
  '''
  
  return '0' * (numOfDigits - len(str(num)))+ str(num) if len(str(num)) < numOfDigits else str(num)

print(myPackaging(5, 22)) # 00022
print(myPackaging(1, 22)) # 22
print(myPackaging(2, 22)) # 22
print(myPackaging(7, 22)) # 0000022
print(myPackaging.__doc__)


