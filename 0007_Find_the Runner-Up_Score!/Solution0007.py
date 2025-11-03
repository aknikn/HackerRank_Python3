n = int(input())
A = input().split(" ")
B = []

# B: an array set the same value as the array A, but as an Integer type
for i in A:
    B.append(int(i))

C = list(set(B))
C.remove(max(C))
print(max(C))