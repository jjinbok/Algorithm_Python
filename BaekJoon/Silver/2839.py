def sugar_div(num):
    cnt = 0

    while num > 0:
        if num % 5 == 0:
            cnt += num // 5
            return cnt
        num -= 3
        cnt += 1
        if num == 0:
            return cnt
    return -1

sugar_total_kg = int(input())

suger_num = sugar_div(sugar_total_kg)
    
print(suger_num)


