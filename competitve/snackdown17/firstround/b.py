def count(input_array, char):
    counter = 0
    for i in input_array:
        if char==i:
            counter+=1
    return counter


def first_char(input_array):
    for i in input_array:
        if i != '.':
            return i
    return '.'


def index_first_char(input_array):
    for i in range(0, len(input_array)):
        if input_array[i] != '.':
            return i


def two_consecutive(input_array):
    char = first_char(input_array)
    index = index_first_char(input_array)
    for i in range(index+1, len(input_array)):
        if input_array[i] == char:
            return True
        elif input_array[i] != '.':
            char = input_array[i]
    return False


def check(input_array):
    first = first_char(input_array)
    if first == 'H':
        Hcount = count(input_array, 'H')
        Tcount = count(input_array, 'T')
        if Hcount != Tcount:
            return "Invalid"
        if two_consecutive(input_array):
            return "Invalid"
        return "Valid"
    elif first == 'T':
        return "Invalid"
    elif first == '.':
        return "Valid"


n = int(raw_input())
for i in range(0, n):
    t = int(raw_input())
    input_array = list(raw_input())
    if t==len(input_array):
        print check(input_array)
    else:
        print "Invalid"
