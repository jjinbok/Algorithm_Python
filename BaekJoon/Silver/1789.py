num = int(input())

sum = 0
cnt = 0
i = 2
while True:
    sum += i
    cnt += 1
    if sum >= num:
        break
    i += 1

print(cnt)