from collections import deque
n = int(input())
m = int(input())
q = deque()
check = [False]*(n+1)
linked = [[] for _ in range(n+1)]

for _ in range(m) : 
    x,y = map(int,input().split())
    linked[x].append(y)
    linked[y].append(x)

check[1] = True
q.append(1) 
while q : 
    x = q.popleft()
    for i in linked[x] : 
        if check[i] == False : 
            check[i] = True 
            q.append(i)

print((check.count(True))-1)

