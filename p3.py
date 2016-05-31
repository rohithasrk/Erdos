x = 1
N = 1

def f(n,y):
	z = (n*(y**2)+1)**(0.5)
	return z

def pfsq(n):				#to check if n is a perfect square.
	sqt = n**(0.5)
	if int(sqt)==sqt:
		return True
	else:
		return False

flist=[]
nlist=[]	
for n in range(2,100000):
	if not pfsq(n):
		y=1
		nlist.append(n)
		while int(f(n,y))!=f(n,y) and n!=61 and n!=109:
			nex = f(n,y+1)
			if int(nex)==nex :
				flist.append(nex)
				print n,
				print nex
			y+=1
print f(2,3)
