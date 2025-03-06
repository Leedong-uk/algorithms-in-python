# 1: 여분 / 0 : 빌릴필요 x  / -1 : 빌려야한다
answer = 0 
n = 5
lost = [2,4]
reserve = [1,3,5]
student = [0]*(n+2)

for i in reserve : 
    student[i] +=1

for i in lost : 
    student[i] -=1 

for i in range(1,n+1) : 
    if student[i] >0 : 
        front = i-1
        back = i+1

        if student[front] < 0 :
            student[front] +=1
            student[i] -=1
        elif student[back] < 0 :
            student[back] +=1
            student[i] -=1 

answer = 0
for i in range(1,n+1) : 
    if student[i] >=0 : 
        answer +=1
print(answer)