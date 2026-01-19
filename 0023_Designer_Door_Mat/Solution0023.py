# Enter your code here. Read input from STDIN.
# Print output to STDOUT
nm = input().split(' ')
N = int(nm[0])
M = int(nm[1])
halfN = N // 2
welcome = 'WELCOME'
centreHyphens = (M-len(welcome))//2
hyphen = '-'
triangle = '.|.'

# upper half
for i in range(halfN):
    triCnt = 2*i+1
    hyphenCnt = (M-3*triCnt)//2
    print(hyphenCnt*hyphen+triCnt*triangle+hyphenCnt*hyphen)
    
# welcome row
print(centreHyphens*hyphen+welcome+centreHyphens*hyphen)

# bottom half
for i in range(halfN-1, -1, -1):
    triCnt = 2*i+1
    hyphenCnt = (M-3*triCnt)//2
    print(hyphenCnt*hyphen+triCnt*triangle+hyphenCnt*hyphen)