x = 1
N = 2
def f(n,y):
	z = (n*(y**2)+1)**(0.5)
	return z

def pfsq(n):				#to check if n is a perfect square.
	sqrt = n**(0.5)
	if int(sqrt)==sqrt:
		return True
	else:
		return False
	
for n in range(1,100000):
	if not pfsq(n):
		for y in range(1,100000):
			if int(f(n,y))==f(n,y):
				if f(n,y)>x:
					x=f(n,y)
					N=n	
				break
print N
