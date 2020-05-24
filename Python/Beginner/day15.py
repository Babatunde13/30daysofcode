def uncensor(str1, str2):
  '''
  A function that replaces the occurences of '*' with the appropriate letter.
  '''
  vowels, i, new_str = 'aeiouAeiou', 0, ''
  for char in str1:
    if char == '*' and str2[i] in vowels:
      new_str += str2[i]
      i +=1
    else: new_str += char
  return new_str