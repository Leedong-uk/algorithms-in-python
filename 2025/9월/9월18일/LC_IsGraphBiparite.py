from collections import deque
def isBipartite(graph) : 
    q = deque()
    n = len(graph)
    color = [False] * n
    color[0] = 0
    q.append(0)
    
    while q : 
        x = q.popleft()
        curr_color = color[x]
        for i in graph[x] : 
            if not color[i]  : 
                color[i] = (curr_color +1)%2
                q.append(i)
            else : 
                if curr_color == color[i] : 
                    return False
    print(color)
    
    return True


print(isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
print (isBipartite([[1,3],[0,2],[1,3],[0,2]]))