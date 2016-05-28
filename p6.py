def sumOfDigits(n):
	sum=0
	while(n>0):
		sum+=n%10
		n/=10
	return sum

n = 3334**3334
A = sumOfDigits(n)
B = sumOfDigits(A)

print 2013*sumOfDigits(B)
