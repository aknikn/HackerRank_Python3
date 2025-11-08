n = int(input())
studentDic = {} # Dictionary(student:[scores])

for _ in range(n):
    name, *iScores = input().split()
    fScores = list(map(float, iScores))
    studentDic[name] = fScores
    
queryName = input()
queryScore = []
sumfScores = 0

scoreArray = studentDic.get(queryName)
for i in range(0, 3):
    sumfScores += scoreArray[i]

print(format(sumfScores/3, '.2f'))