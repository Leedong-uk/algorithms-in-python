from collections import defaultdict
def solution(n,wires) : 
    answer = 0 
    linked_list = defaultdict(list)
    tmp = [0] * (n+1)

    for x , y in wires : 
        linked_list[x].append(y)
        linked_list[y].append(x)
        

    def dfs(curr,parent) : 
        cnt = 1
        for next in linked_list[curr] : 
            if next != parent : 
                cnt += dfs(next,curr)
        tmp[curr] = cnt 
        return cnt 

    dfs(1,None)  
    answer = float('inf')
    
    for i in range(1,n+1) : 
        answer = min(abs(n-tmp[i]*2),answer)
    
    
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
# print(solution(4,[[1,2],[2,3],[3,4]]))