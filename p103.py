def toString(List):
	return ''.join(List)
anslist=[]
def permute(a,l,r):
	if l==r:
		ans=int(toString(a))
		if ans%7==0 and ans%10==3:
                        anslist.append(ans)
	else:
		for i in xrange(l,r+1):
			a[l],a[i] = a[i],a[l]
			permute(a,l+1,r)
			a[l],a[i]=a[i],a[l]

permute(list('3333337'),0,6)
permute(list('3333377'),0,6)
permute(list('3333777'),0,6)
permute(list('3337777'),0,6)
permute(list('3377777'),0,6)
permute(list('3777777'),0,6)

print sum(set(anslist))
