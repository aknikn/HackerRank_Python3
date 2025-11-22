S = input()
sList = list(S)

for i in range(0, 5):
    flg = False
    for s in range(0, len(S)):
        match i:
            case 0:
                if sList[s].isalnum():
                    flg = True
            case 1:
                if sList[s].isalpha():
                    flg = True
            case 2:
                if sList[s].isdigit():
                    flg = True
            case 3:
                if sList[s].islower():
                    flg = True
            case 4:
                if sList[s].isupper():
                    flg = True
    print(flg)