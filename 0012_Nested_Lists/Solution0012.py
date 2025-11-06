N = int(input())
records = []
scores = []
names = []

for i in range(0, N):
    tmp = []
    tmp.append(input())
    score = float(input())
    scores.append(score)
    tmp.append(score)
    records.append(tmp.copy())

minScore = min(scores)
for m in range(0, len(scores)):
    if scores[m] == minScore:
        records[m][1] = 500
        scores[m] = 500

minScore = min(scores)
for j in range(0, len(scores)):
    if records[j][1] == minScore:
        names.append(records[j][0])

names.sort()
for k in range(0, len(names)):
    print(names[k])