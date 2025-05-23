from collections import deque
start , goal = map(int,input().split())
q = deque()
MAX  = 200001
check = [-1] * MAX


check[start] = 0 
q.append(start)

while q : 
    x = q.popleft()
    value = check[x]
    for next in [x*2,x+1,x-1] : 
        if 0<= next <MAX and check[next] == -1: 
            check[next] = value+1
            q.append(next)

print(check[goal])
    

