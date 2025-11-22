def split_and_join(line):
    # write your code below
    lineArray = line.split(" ")
    str = ""
    laLen = len(lineArray)
    
    for i in range(0, laLen):
        if i == laLen-1:
            str += lineArray[i]
        else:
            str += lineArray[i] + "-"

    return str
    # write your code above
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)