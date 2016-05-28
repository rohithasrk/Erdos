from p6 import *

def isPrime(n):
	nfact = 0
	sqrt = n**(0.5)
	for i in range(2,int(sqrt)):
		if n%i==0:
			return False
	if nfact==0: return True

"""Sum = 0
for i in range(0,10**9):
	if isPrime(i):
		Sum+=i
print sumOfDigits(Sum)"""
