#2461828588.7945285
#2640017217.689492
def nofDi(n):
	ans=0
	while n>0:
		ans+=1
		n/=10
	return ans
	
def doubdevils(n):
	toStr=str(n)
	n=list(toStr)
	a=[n[0],n[2],n[4],n[6],n[8],n[10],n[12],n[14],n[16],n[18]]
	b=['6','6','6','0','0','6','6','6','0','0']
	if a==b:return True
	else: return False
	#print nlist

x=2461828588

while not doubdevils(x**2):
	x+=1
print x
