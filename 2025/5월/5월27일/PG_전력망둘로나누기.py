def solution (n,wires) : 
    check = [False] * (n+1)
    linekd_list = [[] for _ in range(n+1)]
    dist = [0] * (n+1)   
    for i in wires : 
        x ,y = i 
        linekd_list[x].append(y)
        linekd_list[y].append(x)
    
    
    
    def dfs(curr,parent) : 
        check[curr] = True
        cnt = 1 
        
        for i in linekd_list[curr] : 
            if i == parent : 
                continue
            
            if check[i] == False : 
                cnt += dfs(i,curr)
        dist[curr] = cnt
        return cnt
    
    dfs(1,None)
    answer = min(map(lambda x : abs(n-2*x),dist))
    return answer

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
