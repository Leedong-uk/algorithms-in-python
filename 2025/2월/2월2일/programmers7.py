from itertools import combinations
nums = [1,2,3,4]
n = sum(sorted(nums,reverse = True)[:3])
number = [True] *(n+1)
number[0] = False
number[1] = False
answer = 0
nums = list(combinations(nums,3))

for i in range(2,int(n**0.5)+1) : 
    for j in range(i*2,n+1,i) : 
        number[j] = False

for i in nums : 
    temp = sum(i)
    if number[temp] : 
        answer +=1
print(answer)


