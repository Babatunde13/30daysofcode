def Santa(numOfSibling: int, numOfSweet: int) -> str:
  '''
  A function named santa which checks if second parameter(number of sweet) can shared evenly between fisrt  parameter(number of siblings).

  Parameter: ----------
            numOfSibling: int, number of siblings that wants to share the sweet
            
            numOfSweet: int, number of sweet to be shared evenly by the siblings.

  Returns: ---------------
            'give away' if sweet can be shared evenly among siblings, otherwise 'eat them yourself'
        
  @author: Babatunde Koiki
  Created on: 03-05-2020
  '''
  return 'give away' if numOfSweet % numOfSibling == 0 else 'eat them yourself'

print(Santa(3, 9))
print(Santa(3, 8))
print(Santa(4, 7))
print(Santa.__doc__)
