def validator(email, password):
  '''
  A function that validates a user login details
  '''
  res = {
    'email': 'false', 'password': 'false'
  }
  if any([x.islower() for x in password]) and any([x.isupper() for x in password]) and any([not x.isalnum() for x in password]) and any([x.isdigit() for x in password]) and len(password) >= 8: res['password'] = 'true'
  before_at = email[:email.index('@')]
  after_at = email[email.index('@'):]

  if any([x.isprintable() for x in before_at]):
    if (after_at.count('.')==1 and 3<= len(after_at[after_at.index('.'):]) <=4) or (after_at.count('.')==2 and 7<= len(after_at[after_at.index('.'):]) <=8) : res['email'] = 'true'


  return res



 