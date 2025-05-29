from collections import deque

k = int(input())
w, h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(h)]


check = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]


horse_x = [-1, -1, -2, -2, 1, 1, 2, 2]
horse_y = [2, -2, -1, 1, 2, -2, 1, -1]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


q = deque()
check[0][0][0] = 0
q.append((0, 0, 0)) 

while q:
    x, y, z = q.popleft()

    
    if x == h - 1 and y == w - 1:
        print(check[x][y][z])
        exit()

    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if maps[nx][ny] == 0 and check[nx][ny][z] == -1:
                check[nx][ny][z] = check[x][y][z] + 1
                q.append((nx, ny, z))

   
    if z < k:
        for i in range(8):
            nx, ny = x + horse_x[i], y + horse_y[i]
            if 0 <= nx < h and 0 <= ny < w:
                if maps[nx][ny] == 0 and check[nx][ny][z + 1] == -1:
                    check[nx][ny][z + 1] = check[x][y][z] + 1
                    q.append((nx, ny, z + 1))


result = [x for x in check[h-1][w-1] if x != -1]

if result : 
    print(min(result))
else : 
    print(-1)
    

