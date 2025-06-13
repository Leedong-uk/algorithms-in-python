from itertools import combinations
n = 4 
k = 2

number = [x for x in range(1,n+1)]
answer = []

def dfs(start,sum) :
    if len(sum) == k : 
        answer.append(sum)
    
    for i in range(start,len(number)) : 
        dfs(i+1,sum+[number[i]])

dfs(0,[])
print(answer)