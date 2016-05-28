from p8 import *

f = open("p12","r+")
x = f.read()
lines = x.split('\n')
#print len(lines)
del lines[len(lines)-1]
#print len(lines)

sortedlist=[]
for i in range(len(lines)):
	if isPrime(int(lines[i])):
		sortedlist.append(int(lines[i]))

#sortedlist=sorted(sortedlist)
difflist=[]
for i in range(1,len(sortedlist)):
	difflist.append(sortedlist[i]-sortedlist[i-1])
print max(difflist)
