# as k=(4128**6+6**4128)
# we get k%4==0 and k%2==0

def unitd(n):
	plist=[0,1,6,1,6,5,6,1,6,1]
	return plist[n]
ans=0
for i in range(1,17040385):
	ans+=unitd(i%10)
print ans
