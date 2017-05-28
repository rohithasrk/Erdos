def prodOfDig(n):
	pro=1
	while n>0:
		pro=pro*(n%10)
		n=n/10
	return pro

number=0
for i in range(11111,100000):
	if prodOfDig(i)!=0 and prodOfDig(i)%10==0:
		number+=1

print number
