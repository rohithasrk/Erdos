an=0.0
n=1
while True:
	num=2**n
	num=list(str(num))
	if num[0]=='1':
		an+=1.0;
		print (an/n)*(10**6)
	n+=1

#print 2.0/3
