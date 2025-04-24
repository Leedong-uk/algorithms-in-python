# bfs
from collections import deque
n = int(input()) +1
m = int (input())
linked_list = [[] for _ in range(n)]
q = deque()
check = [False] * n
cnt = 0

for _ in range(m) : 
    x ,y = map(int,input().split())
    linked_list[x].append(y)
    linked_list[y].append(x)

check[1] = True # 해도되고 안해도 되고
check[1] = True
q.append(1)


while q : 
    x = q.popleft()
    for i in linked_list[x] : 
        if check[i] == False : 
            check[i] = True
            q.append(i)
            cnt +=1
print(cnt)



# dfs
n = int(input()) +1
m = int (input())
linked_list = [[] for _ in range(n)]
check = [False] * n
cnt = 0

for _ in range(m) : 
    x ,y = map(int,input().split())
    linked_list[x].append(y)
    linked_list[y].append(x)


def bfs(start) : 
    global cnt
    check[start] = True 
    for i in linked_list[start] : 
        if check[i] == False :
            cnt +=1
            check[i] = True
            bfs(i)
            

bfs(1)
print(cnt)
    
    