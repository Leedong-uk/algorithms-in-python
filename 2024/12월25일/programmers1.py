from itertools import combinations
k = 2
tangerine =[1, 1, 1, 1, 2, 2, 2, 3]
tangerine_dic ={}

for i in tangerine :
    if i in tangerine_dic : 
        tangerine_dic[i] +=1 
    else :
        tangerine_dic[i] = 1

tangerine_dic = dict(sorted(tangerine_dic.items(), key=lambda x: x[1], reverse=True))

result = 0
cnt = 0
for i in tangerine_dic : 
    result = result + tangerine_dic[i]
    if result >=k :
        cnt +=1
        answer = cnt
        break
    else : cnt +=1


print(answer)





    
    
