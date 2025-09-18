from collections import deque
def solution(n,vertex) : 
    answer = 0
    q = deque()
    linked_list = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    for i in vertex : 
        x,y = i 
        linked_list[x].append(y)
        linked_list[y].append(x)
    
    visited[0] = 0
    visited[1] = 0
    cnt = 0 
    q.append(1)
    
    while q: 
        x = q.popleft()
        
        for i in (linked_list[x]) : 
            if visited[i] == -1 : 
                visited[i] = visited[x] +1
                q.append(i)
    print(visited)
    max_distance = max(visited)
    answer = visited.count(max_distance)
    
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))