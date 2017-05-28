def pfsq(n):
	s = int(n**0.5)
	#print s
	#print n**0.5
	return s**2==n

def isfibo(n):
	return pfsq(5*n**2+4) or pfsq(5*n**2-4)

f=open('p14.txt','r')
flist = f.read().split('\n')
#print flist
flist.pop()
number=0
for i in flist:
	if isfibo(int(i)):
		number+=1
print number
