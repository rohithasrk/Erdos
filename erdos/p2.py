def final(x):
	y = (x**6+8*(x**4)-6*(x**2)+8)**(1.0/6)
	z = 3345*x+4321*(y**2)
	if x>0 and y>0 and int(z) == z :
		return z
	else:
		return 0

def f(x):
	return (x**6+8*(x**4)-6*(x**2)+8)**(1.0/3)
i = 0.0

while(not final(i/3345)):
	j=i+1.0
	if final(j/3345):
		print final(j/3345)	
	i+=1.0
