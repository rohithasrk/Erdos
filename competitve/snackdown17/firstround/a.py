def check(input_array):
    t = len(input_array)
    ini = t/2
    maxi = ini + 1
    if t%2==1:
        for i in range(1, t+1):
            if i<=ini:
                if input_array[i-1]!=i:
                    return 'no'
            elif i>ini:
                if input_array[i-1]!=2*maxi-i:
                    return 'no'
        return 'yes'
    else:
        return 'no'
            
n = int(raw_input())
for i in range(0, n):
    t = input()
    input_array = map(int, raw_input().split())
    print check(input_array)
