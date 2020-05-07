def expensereport(text: str) -> str:
    '''
    A function that takes in a multiline string and makes a report on it, 
    then returns the report as a multiline string.

    @author: Babatunde Koiki
    Created on: 07-05-2020
    '''
    text = [x.split() for x in text.split('\n')] # Turning the multiline string to a list of list.
    n = float(text[0][0]) #Getting the initial price.
    price, res = n, f'Original_Balance:_{text[0][0]}'

    for x in text[1:]:
        price -= float(x[-1])
        x.extend(['Balance', str(round(price, 2))])
        i='\n'+'_'.join(x)
        res+=i
        if i[::-1].index('.') < 2: res+= '0'* (2 - i[::-1].index('.'))

    a = f'\n{int(text[-1][0])+1}_Neighbor_50.00_Balance_{str(round(price-50, 2))}'
    b = f'\nTotal_expense__{str(round(n-price+50, 2))}'
    avg = (n-price+50)/(int(text[-1][0])+1) # Average expense
    c=f'\nAverage_expense__{str(round(avg, 2))}'
    res+=a+b+c
    return res 

print(expensereport('''1000.00
1 Market 125.45
2 Hardware 34.95
3 Video 7.45
4 Book 14.32
5 Gasoline 16.10'''))

