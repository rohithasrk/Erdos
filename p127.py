def powof2(n):
	power=0
	while(not n&1):
		power+=1
		n/=2
	return power

n=2
x=0
while n<=4444444444:
	if powof2(n)%2==0:
		x+=1
	n+=2

print x+2222222222
