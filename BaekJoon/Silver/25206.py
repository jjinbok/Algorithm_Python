subject_avg_score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

subject = []
subject_score_sum = 0
user_subject_score_sum= 0

for i in range(0,20):
    subject.append(input().split())
    if subject[i][2] == 'P': continue
    user_subject_socre = subject_avg_score[subject[i][2]]
    subject_score_sum += (float)(subject[i][1])
    user_subject_score_sum += (float)(subject[i][1]) * user_subject_socre
    
total_score = user_subject_score_sum / subject_score_sum

print(total_score)

