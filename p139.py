def pfnumber(n):
	return (2**(n-1))*(2**n-1)

def isPrime(n):
        nfact = 0
        sqrt = n**(0.5)
        for i in range(2,int(sqrt)+1):
                if n%i==0:
                        return False
        if nfact==0: return True

def Mprime(p):
	return 2**p-1

mod=10**9+7
Nmax=5*(10**35)
pfsum=0
n=1

while pfnumber(Mprime(n))<=Nmax:
	if isPrime(Mprime(n)):
		pfsum+=pfnumber(Mprime(n))
		print pfsum
	n+=1

print isPrime(6)
print pfsum
print pfsum%mod
