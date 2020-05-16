from datetime import datetime
def date():
  '''
  A function that returns the current date in twi different formats.
  @author:Babatunde Koiki
  Created on 09-05-2020
  '''
  
  return {
    'v1': datetime.now().strftime('%d/%m/%y'),
    'v2': datetime.now().strftime('%m/%d/%y')
  }


