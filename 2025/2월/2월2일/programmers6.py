answer = [1,2,3,4,5]
std1=[1,2,3,4,5]
std2=[2,1,2,3,2,4,2,5]
std3=[3,3,1,1,2,2,4,4,5,5]

cnt1 = 0
cnt2 = 0
cnt3 = 0

for i in range(len(answer)) : 
    if answer[i] == std1[i%5] : 
        cnt1 +=1
    if answer[i] == std2[i%8] : 
        cnt2 += 1
    if answer[i] == std3[i%10] : 
        cnt3 += 1

mac= max(count1,count2,count3)

if mac == cnt1 :  
    answer.append(1)
if mac == cnt2 : 
    answer.append(2)
if mac == cnt3 : 
    answer.append(3)
answer.sort()
    
