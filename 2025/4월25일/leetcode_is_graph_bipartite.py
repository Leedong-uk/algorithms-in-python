from collections import deque

graph = [[1,3],[0,2],[1,3],[0,2]]
n = len(graph)
check = [-1] * n  

def bfs(start):
    q = deque()
    q.append(start)
    check[start] = 0  

    while q:
        x = q.popleft()
        for i in graph[x]:
            if check[i] == -1:
                check[i] = 1 - check[x]  
                q.append(i)
            elif check[i] == check[x]: # 같은 그룹 내에 간선이 존재 하면 안됨으로 
                return False  
    return True

output= True
for i in range(n):
    if check[i] == -1:
        if bfs(i) == False:
            output = False
            break

print(output)
