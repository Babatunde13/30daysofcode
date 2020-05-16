def naruto(n: int) -> list:
  '''
  A function that takes in an integer and returns an array of element in a particular order.
  @author: Babatunde Koiki
  Created on: 09-05-2020
  '''
  l = [1]
  for i in range(2, n+1):
    if i % 2 == i%3==i%5: l.append('Na-Ru-To')
    elif i%2==i%3==0: l.append('Na-Ru')
    elif i%2==i%5==0: l.append('Na-To')
    elif i%5==i%3==0: l.append('Ru-To')
    elif i%2==0: l.append('Na')
    elif i%3==0: l.append('Ru')
    elif i%5==0: l.append('To')
    else: l.append(i)
  return l

