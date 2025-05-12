from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

m = len(grid)       
n = len(grid[0])    
check = [[-1] * n for _ in range(m)]
cnt = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == "1" and check[i][j] == -1:
            cnt += 1
            q.append((i, j))
            check[i][j] = cnt

            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == "1" and check[nx][ny] == -1:
                            check[nx][ny] = cnt
                            q.append((nx, ny))

print(cnt)
