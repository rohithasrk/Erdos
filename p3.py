x = 1
def f(n,y):
	z = (n*(y**2)+1)**(0.5)
	if int(z)==z:
		return z
	else:
		return 1
	
for n in range(2,100001):
	y = 1.0
	while(f(n,y)==1):
		if x<f(n,y):
			x=f(n,y)	
		y+=1.0
print x
