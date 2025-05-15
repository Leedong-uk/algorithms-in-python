from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
check = [[False]*m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = -1  

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    check[start_x][start_y] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny] and board[nx][ny] == -1:
                    check[nx][ny] = True
                    q.append((nx, ny))
                    cnt += 1
    return cnt

max_value = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == -1 and not check[i][j]:
            max_value = max(max_value, bfs(i, j))

print(max_value)
