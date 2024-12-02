from collections import deque
n , m = map(int,input().split())
a = list(range(101))
dist = [-1]*101
q = deque()

for _ in range(n+m) : 
    x , y = map(int,input().split())
    a[x] = y 

dist[1] = 0
q.append(1)

while q : 
    x = q.popleft()
    
    for i in range(1,7) : 
        y = x + i

        if y > 100 :
            continue

        y = a[y]
        if dist[y] == -1 : 
            dist[y] = dist[x]+1
            q.append(y)

print(dist[100])

