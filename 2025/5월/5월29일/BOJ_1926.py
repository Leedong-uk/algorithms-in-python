from collections import deque

n, m = map(int, input().split())  # n: 세로, m: 가로
maps = [list(map(int, input().split())) for _ in range(n)]  # n줄 입력 받기
check = [[False] * m for _ in range(n)]  # 방문 여부

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    check[start_x][start_y] = True
    area = 1  # 그림 넓이

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not check[nx][ny] and maps[nx][ny] == 1:
                    check[nx][ny] = True
                    q.append((nx, ny))
                    area += 1
    return area

picture_count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if not check[i][j] and maps[i][j] == 1:
            picture_count += 1
            max_area = max(max_area, bfs(i, j))

print(picture_count)
print(max_area)
