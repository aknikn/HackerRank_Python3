n = int(input())
list = []

for _ in range(n):
    command, *nums = input().split(' ')
    match command:
        case 'insert':
            list.insert(int(nums[0]), int(nums[1]))
        case 'print':
            print(list)
        case 'remove':
            list.remove(nums[0])
        case 'append':
            list.append(nums[0])
        case 'sort':
            list.sort()
        case 'pop':
            list.pop(-1)
        case 'reverse':
            list.reverse()