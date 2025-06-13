answer= []
nums = [1,2,3]


def dfs(nums,end,start,sum,result) : 
    
    if len(sum) == end : 
        result.append(sum)
        return result
    
    for i in range(start,len(nums)) : 
        dfs(nums,end,i+1,sum+[nums[i]],result)

for end in range(len(nums) + 1):
    result = []
    dfs(nums,end, 0, [], result)
    answer.append(result)
    
    

print(answer)



