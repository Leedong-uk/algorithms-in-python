from collections import deque

maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]
check = [[-1]*5 for _ in range(5)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

q.append((0, 0))
check[0][0] = 0

while q: 
    x, y = q.popleft()
    value = check[x][y]
    for k in range(4): 
        nx, ny = x + dx[k], y + dy[k]  
        if (0 <= nx < 5 and 0 <= ny < 5) and check[nx][ny] == -1 and maps[nx][ny] == 1:
            q.append((nx, ny))
            check[nx][ny] = value + 1

print(check[4][4]+1)
