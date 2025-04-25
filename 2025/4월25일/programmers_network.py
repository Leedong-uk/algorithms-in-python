from collections import deque
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
check = [False] * (n)
cnt = 0


def bfs(start): 
    q = deque()
    q.append(start)
    check[start] = True
    
    while q : 
        x = q.popleft()
        for index , value in enumerate(computers[x]) : 
            if value == 1 and check[index] == False : 
                check[index] = True
                q.append(index)


for i in range(n) : 
    if check[i] == False : 
        bfs(i)
        cnt +=1

print(cnt)


