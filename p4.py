def toHex(n):
	if(n==0): return str(0)
	hexStr = ""
	hexList = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
	rem = n%16
	hexStr = str(hexList[rem])+hexStr
	return toHex(n/16)+hexStr

def pal(s):
	l = len(s)
	check = 0
	for i in range(l):
		if s[i] == s[l-1-i] :
			check+=1
	if check==l:
		return True
	else:
		return False

def sumOfPals(n):
	palSum = 0
	for i in range(n):
		Oct = oct(i)[2:]
		Bin = bin(i)[2:]
		Hex = hex(i)[2:]
		if pal(Hex):
			if pal(Oct):
				if pal(Bin):
					palSum+=i
	return palSum

print sumOfPals(10**9+1)
		
