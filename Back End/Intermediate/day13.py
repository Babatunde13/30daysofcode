def convert(num):
  '''
  A function that converts integers to words.
  '''
  import inflect
  return inflect.engine().number_to_words(num).replace('-', ' ').replace(' and', '').replace(',', '')

print(convert(2032))
print(convert(1234567890))