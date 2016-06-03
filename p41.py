def noOfones(n):
	number=0
	while n>0:
		if n%10==1:
			number+=1
		n/=10
	return number

n=123456790
ans=0
while n<1234567890:
	ans+=noOfones(n)
	n+=1
print ans
