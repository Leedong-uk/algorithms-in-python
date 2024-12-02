#마지막 자리수가 0이면서 각 자리의 수의 합이 3의 배수를 만족한다
def check_3 (nums) : 
    tmp = 0
    for i in nums : 
        tmp += i

    if tmp%3 == 0 :
        return True
    return False

        

nums = list(map(int,input()))
n = len(nums)
nums.sort()
nums.reverse()

if check_3(nums) and nums[n-1] == 0:
    print("".join(map(str,nums)))
else:
    print(-1)


