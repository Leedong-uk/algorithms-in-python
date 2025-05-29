from collections import deque,defaultdict
def solution(info,edges) : 
    linked_list  = defaultdict(list)
    max_sheep = 0
    visited = [False] * len(info)
    for x , y in edges : 
        linked_list[x].append(y)
    def dfs(curr,sheep,wolf,next) : 
        nonlocal max_sheep
        
        if info[curr] == 0 : 
            sheep+=1
        else : 
            wolf +=1
        
        if wolf >= sheep : 
            return
        
        max_sheep = max(max_sheep,sheep)
        visited[curr] = True
        
        for child in linked_list[curr]:
            next.append(child)
        
        for i in range(len(next)):
            next_node = next[i]
        if not visited[next_node]:
            next_available = next[:i] + next[i+1:]
            dfs(next_node, sheep, wolf, next_available)
        visited[curr] = False
        
        return max_sheep
            
                
                
            

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0],[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))