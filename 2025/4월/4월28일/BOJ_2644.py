from collections import deque
n = int(input()) 
start, end = map(int, input().split())  
m = int(input()) 
linked_list = [[] for _ in range(n+1)]  
check = [-1] * (n+1)

for _ in range(m):  
    x, y = map(int, input().split()) 
    linked_list[x].append(y)
    linked_list[y].append(x)

def bfs (start) : 
    q = deque()
    q.append(start)
    check[start] = 0 
    while q: 
        x = q.popleft()
        value = check[x]
        for i in linked_list[x] : 
            if check[i] == -1 : 
                q.append(i)
                check[i] = value+1

bfs(start)
print(check[end])


