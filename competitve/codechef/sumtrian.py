t = int(raw_input())
lead = []
for i in range(0, t):
    n = map(int, raw_input().split())
    lead.append(n[0]-n[1])

a_lead = max(lead)
b_lead = -1*min(lead)

if a_lead>b_lead:
    print 1,a_lead
else: print 2,b_lead
