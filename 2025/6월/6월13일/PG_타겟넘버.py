def solution(numbers, target):
    answer = 0  
    cnt = 0
    
    def dfs(depth , target , curr ) : 
        nonlocal cnt
        if depth == len(numbers) : 
            if curr == target :
                cnt +=1
            return 
        
        
        dfs(depth+1,target,curr+numbers[depth])
        dfs(depth+1,target,curr-numbers[depth])
            
    dfs(0,target,0)
    return cnt


print(solution([1, 1, 1, 1, 1],3))
# print(solution([4, 1, 2, 1],4))