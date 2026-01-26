def print_rangoli(size):
    # my code goes below
    data = "abcdefghijklmnopqrstuvwxyz"
    alpha = [data[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1]+items[::-1]
    
    for i in items:
        temp = alpha[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))

# my code goes above
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)