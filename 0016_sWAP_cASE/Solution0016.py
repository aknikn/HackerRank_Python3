def swap_case(s):
# Write my code below
    result = ""
    sArray = list(s)
    for i in sArray:
        if i.isupper():
            result += i.lower()
        elif i.islower():
            result += i.upper()
        else:
            result += i
    return result

# Write my code above
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)