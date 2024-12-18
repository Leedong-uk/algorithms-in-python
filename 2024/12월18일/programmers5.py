number = 5
limit = 3
power = 2
result = []
answer = 0
for n in range(1,number+1):
    temp = 0
    for i in range(1,int(n**(0.5))+1) :
        if n%i == 0 :
            temp +=1 
            if((i**2) != n) :
                temp +=1
    result.append(temp)

for j in result : 
    if j > limit : 
        answer += power
    else : 
        answer +=j

print(answer)

            
