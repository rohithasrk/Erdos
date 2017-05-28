def fac(n):
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact

t = input()
for i in range(0,t):
    n = input()
    print fac(n)
