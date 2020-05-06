def Zeros(n):
	'''
	A function that returns the number of trailing zeros after computing the factorial of it's parameter

	Parameter: n: int, number to calculate the number of trailing zeros in it's factorial.

	Returns: number of trailiing zeros.

	@author: Babatunde Koiki
	Created on: 06-05-2020 
	'''
	def fact(y):
		f = 1
		for _ in range(y, 0, -1):
			f *= _
		return str(f)[::-1] 
	count = 0
	for i in fact(n):
		if i != '0':
			return count
		else: count +=1

print(Zeros(6))