# Enter your code here.
# Read input from STDIN.
# Print output to STDOUT

n = int(input())
tList = list(map(int, input().split(" ")))
t = tuple(tList)
print(hash(t))