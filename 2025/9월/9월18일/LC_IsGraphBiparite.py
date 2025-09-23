from collections import deque
def isBipartite(graph) : 
    q = deque()
    n = len(graph)
    color = [-1] * n
    for start in range(n) : 
        if color[start] == -1 : 
            q.append(start)
            color[start] = 0
        while q : 
            x = q.popleft()
            curr_color = color[x]
            for i in graph[x] : 
                if color[i] == -1  : 
                    color[i] = (curr_color +1)%2
                    q.append(i)
                else : 
                    if curr_color == color[i] : 
                        return False
        
    return True
    

print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print (isBipartite([[1,3],[0,2],[1,3],[0,2]]))