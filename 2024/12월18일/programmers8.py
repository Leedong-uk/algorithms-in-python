nums= [1,2,3,4]

answer = 0
n = max(nums)
number = [True] * (n+1)
number[0] = False
number[1] = False
    
for i in range(2,int((n+1)**0.5)+1) : 
    for j in range(i*2,n+1,i) : 
        number[j] = False
    
for i in range(len(nums)-2) : 
    for j in range(i+1,len(nums)-1) :
        for k in range(j+1,len(nums)) : 
            if number[nums[i] + nums[j] + nums[k]] : 
                print(i,j,k)
                answer +=1
print(answer)


nums = [1, 2, 3, 4]
answer = 0
n = max

# 에라토스테네스의 체로 소수 판별
number = [True] * (n + 1)
number[0] = number[1] = False

for i in range(2, int(n**0.5) + 1):
    if number[i]:
        for j in range(i * i, n + 1, i):
            number[j] = False

# 삼중 for문으로 조합 탐색
for i in range(len(nums) - 2):
    for j in range(i + 1, len(nums) - 1):
        for k in range(j + 1, len(nums)):
            total = nums[i] + nums[j] + nums[k]
            if number[total]:  # 합이 소수인지 확인
                print(f"조합: {nums[i]}, {nums[j]}, {nums[k]} -> 합: {total}")
                answer += 1

print(f"소수인 조합의 개수: {answer}")
