def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

find_num_cnt = int(input())
find_num = list(map(int, input().split()))

find_num.sort()

compare_num_cnt = int(input())
compare_num = list(map(int, input().split()))

found_flags = [1 if binary_search(num, find_num) else 0 for num in compare_num]

for flag in found_flags:
    print(flag)

