import math

num = int(input())

save_score = []
for i in range(0,num):
    score = 0
    answer = input()
    splitX = answer.split('X')
    for j in range(0,len(splitX)):
        score += (int)(math.pow(len(splitX[j]),2) + len(splitX[j])) // 2
    save_score.append(score)

for i in range(0,num):
    print(save_score[i])