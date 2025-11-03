def inc(start, end):
    result = 0
    for i in range(start, end):
        result = result*10+i
    return result

def dec(start, end):
    result = 0
    i = start
    while i<end:
        result = i*10**(i-1)+result
        i+=1
    return result

# main
N = int(input())
result = 0
normal = 0
reverse = 0

i=1
while(i<N+1):
    normal = inc(1, i+1)
    reverse = dec(1, i)
    if i==1:
        result = normal+reverse
    else:
        result = normal*10**(i-1)+reverse
    print(result)
    i+=1