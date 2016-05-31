def f(n):
	ans=1
	for i in range(1,n+1):
		ans=((ans%2097152)*201413)%2097152
	return ans

print f(1000000000)

	
