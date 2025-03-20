from collections import deque
n , m  , start =  map(int,input().split()) 
linked_list = [[] for _ in range(n+1)] 
q = deque()


def dfs(start) :
    board[start] = True
    print(start,end=' ')
    for i in linked_list[start] : 
        if board[i] == False :
            dfs(i)

def bfs (start) : 
    q.append([start])
    board[start] = True
    while q: 
        x = q.popleft()
        print(x,end=' ')
        for i in linked_list[x] : 
            if board[i] == False : 
                q.append(i)
                board[i] = True

for _ in range(m) : 
    x , y = map(int,input().split())
    linked_list[x].append(y)
    linked_list[y].append(x)

for i in range(1,n+1) : 
    linked_list[i].sort()

board = [False]*(n+1)
dfs(start)
board = [False]*(n+1)
print('')
bfs(start)