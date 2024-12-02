target = int(input())
n = int(input())
broken = list(map(int,input().split()))

#현재 채널에서 +혹은-만 사용하여 이동하는 경우
min_count = abs(100-target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)) : 
        if int(nums[j])in broken : 
            break

        elif j == len(nums)-1 :
            min_count = min(min_count,abs(int(nums)-target)+len(nums))



print(min_count)