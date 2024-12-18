n = 5
number = [True] * 1000001
number[0] = False
number[1] = False
answer = 0

for i in range(2,int(1000001**(0.5)+1)) : 
    for j in range(i*2,1000001,i) : 
         number[j] = False

for i in range(n+1) : 
    if number[i] == True : 
        answer +=1


print(answer)