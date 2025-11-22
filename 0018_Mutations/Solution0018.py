def mutate_string(string, position, character):
    # write my code below
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string
    
    # another solution
    # string = string[:position]+character+string[position+1:]
    # return string
    
    # write my code above
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)