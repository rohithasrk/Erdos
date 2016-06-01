for i in range(100000,166667):
	orig=i
	newn=6*i
	oristr=list(str(orig))
	reqstr=''+oristr[3]+oristr[4]+oristr[5]+oristr[0]+oristr[1]+oristr[2]
	reqn=int(reqstr)
	if newn==reqn:
		print orig
