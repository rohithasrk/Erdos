def facmod(n):
	fac=1
	for i in range(1,1000000009):
		fac=((fac%1000000009)*i)%1000000009
	return fac
print facmod(1000000008)
