#from p8 import *

def isPrime(n):
        nfact = 0
        sqrt = n**(0.5)
        for i in range(2,int(sqrt)):
                if n%i==0:
                        return False
        if nfact==0: return True

f = open("p12.txt","r+")
x = f.read()
lines = x.split('\n')
#print len(lines)
del lines[len(lines)-1]
#print len(lines)
#print lines[534]
lines = sorted(lines)
sortedlist=[]
gap=[]
gapv=0
for i in range(len(lines)):
	if isPrime(int(lines[i])):
		sortedlist.append(int(lines[i]))
		gap.append(gapv)
		gapv=0;
	else:
		gapv+=1;
print gap
print max(gap)
"""print sortedlist
#sortedlist=sorted(sortedlist)
difflist=[]
for i in range(1,len(sortedlist)):
	difflist.append(sortedlist[i]-sortedlist[i-1])
print max(difflist)"""
