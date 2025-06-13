nums = [2,7,11,15]
check = {}
target = 9

for i , number in enumerate(nums) : 
    complement = target - number
    
    if complement in check : 
        [check[complement],i]
    
    check[number] = i

    