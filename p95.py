def canPaid(n):
	x=0
	y=0
	reqform = 7*x+13*y
	mx=int(n/7)
	cons=0
	for i in range(0,mx+1):
		y = (n-7*i)/13
		if int(y)==y:
			cons+=1
	if cons==0:
		return False
	else: return True

number=7.0
while True:
	if not canPaid(number):
		print number
	number+=1.0
		
