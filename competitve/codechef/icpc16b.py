def other_than_0_or_1(array):
    s = list(set(array))
    if 0 in s:
        s.remove(0)
    if 1 in s:
        s.remove(1)
    return s

def count(n, array):
    c = 0
    for i in array:
        if i==n:
            c+=1
    return c
    
def check(array):
    s = list(set(array))
    if len(s)==3:
        if 0 in s and 1 in s:
            x = other_than_0_or_1(s)[0]
            if x==-1:
                return "yes"
            else:
                if count(x, array)>1:
                    return "no"
                return "yes"
        else: return "no"
    elif len(s)==2:
        if 0 in s and 1 in s:
            return "yes"
        elif 0 in s or 1 in s:
            x = other_than_0_or_1(s)[0]
            if x==-1:
                if count(x, array)>1 and 1 in s:
                    return "yes"
                else: return "no"
            if count(x, array)>1:
                return "no"
            return "yes"
        else: return "no"
    elif len(s)==1:
        x = s[0]
        if x==0 or x==1:
            return "yes"
        else:
            if count(x, array)>1:
                return "no"
            else: return "yes"
    else:
        return "no"

t = int(raw_input())
result = []
for i in range(t):
    n = int(raw_input())
    in_array = map(int, raw_input().split())
    if n==len(in_array):
        result.append(check(in_array))
for i in result:
    print i
