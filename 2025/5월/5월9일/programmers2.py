from collections import deque

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

m = len(places)
n = len(places[0])


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(start_x, start_y):
    q = deque()
    check = [[-1] * 5 for _ in range(5)]  
    check[start_x][start_y] = 0  
    q.append((start_x, start_y))

    while q:
        x, y = q.popleft()
        value = check[x][y]

       
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            
            if 0 <= nx < 5 and 0 <= ny < 5 :
                if check[nx][ny] == -1 and places[nx][ny] != "X":
                    check[nx][ny] = value + 1
                    q.append((nx, ny))

                    if places[nx][ny] == "P" and check[nx][ny] <= 2:
                        return False  

    return True 


def find(places):
    for i in range(5):
        for j in range(5):
            if places[i][j] == "P":
                if not bfs(i, j):  
                    return 0  
    return 1  


answer = []

for places in places : 
    answer.append(find(places))

print(answer)
