def myPackaging(numOfDigits: int, num: int) -> str:
  '''
  A functiin named myPackaging which right shitfts a number. It adds zeros to the front of the number.

  Parameters: ----------
  '''
  
  return '0' * (numOfDigits - len(str(num)))+ str(num) if len(str(num)) < numOfDigits else str(num)

