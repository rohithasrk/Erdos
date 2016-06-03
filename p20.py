five=[]
seven=[]
reqlist=[five,seven]

num=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18']

def toString(array):
	return ''.join(array)

def Comb(arr,data,start,end,index,r,x):
	if index==r:
		for j in range(0,r):
			reqlist[x].append(toString(data))
	
	for i in range(start,end+1):
		if end-i+1>=r-index:
			data.append(arr[i])
			Comb(arr,data,i+1,end,index+1,r,x)

for r in range(1,12):
	data=[]
	Comb(num,data,0,11,0,r,0)

print reqlist
