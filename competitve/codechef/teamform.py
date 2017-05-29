def check(n, m, array):
    if max(array)<=n:
        if 2*m==len(set(array)):
            return "yes"
        else:
            return "no"
    else:
        return "no"

t = int(raw_input())
result = []
for i in range(0, t):
    tc = map(int, raw_input().split())
    n, m = tc[0], tc[1]
    m_array = []
    for i in range(0, m):
        l = map(lambda x: m_array.append(int(x)), raw_input().split())
    if n%2==0:
        result.append(check(n, m, m_array))
    else:
        result.append("no")

for i in result:
    print i
