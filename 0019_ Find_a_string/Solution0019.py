def count_substring(string, sub_string):
    # write my code below
    strLen = len(string)
    subLen = len(sub_string)
    result = 0
    
    for i in range(0, strLen-subLen+1):
        if string[i:subLen+i] == sub_string:
            result += 1
            
    return result
    # write my code above
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)