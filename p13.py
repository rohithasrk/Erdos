import sys
orig_stdout = sys.stdout
f = file('p13.txt','w')
sys.stdout = f

def isPrime(n):
        nfact = 0
        sqrt = n**(0.5)
        for i in range(2,int(sqrt)):
                if n%i==0:
                        return False
        if nfact==0: return True

def toString(List):
	return ''.join(List)

def permute(a,l,r):			#a as string converted to a list, l, r as the array indices
	if l==r and a[0]!='0':
		r = toString(a)
		r = int(r)
		if isPrime(r):
			print r
	else:
		for i in xrange(l, r+1):
			a[l],a[i] = a[i],a[l]
			permute(a,l+1,r)
			a[l],a[i] = a[i],a[l]

string='11023456789'
n=len(string)
a=list(string)
permute(a,0,n-1)
