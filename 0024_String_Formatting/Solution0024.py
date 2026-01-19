def print_formatted(number):
    # your code goes below
    for i in range(1, number+1):
        width = len(f'{number:b}')
        print(f'{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}')
    # your code goes above

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)