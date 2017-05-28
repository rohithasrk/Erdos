def f(n):
	return (42.0/n)**n
#print f(5)

N=1;
P=42;
for i in range(1,42):
	if f(i)>P:
		N=i
		P=f(i)
print int(P)
