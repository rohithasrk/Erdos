def fact(n,modulus):
	ans0 = 1
	ans1 = 1
	for i in range(1,(n+1) / 2):
    		ans0 = ans0 * (2*i + 0) % modulus    
    		ans1 = ans1 * (2*i + 1) % modulus    
	return ans0 * ans1 % modulus

print fact(1000000008,1000000009)
