n = int(input())
result = ""

if n%2==1:
    result = "Weird"
elif 6<=n and n<=20:
    result = "Weird"
else:
    result = "Not Weird"

print(result)