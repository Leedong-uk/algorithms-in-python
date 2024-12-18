n = int(input())
board = [ ["." for _ in range(n)] for _ in range(n)]  # 2차원 배열로 변경
command = list(input())
d = [[False for _ in range(n)] for _ in range(n)]
u = [[False for _ in range(n)] for _ in range(n)]
r = [[False for _ in range(n)] for _ in range(n)]
l = [[False for _ in range(n)] for _ in range(n)]
current_location = [0, 0]  # 리스트로 변경
next_location = [0, 0]

for i in command:
    if i == "D":
        if current_location[0] + 1 < n:
            next_location = [current_location[0] + 1, current_location[1]]
            d[current_location[0]][current_location[1]] = True
            d[next_location[0]][next_location[1]] = True
            current_location = next_location  # 리스트로 전체 교체
    elif i == "U":
        if current_location[0] - 1 >= 0:
            next_location = [current_location[0] - 1, current_location[1]]
            u[current_location[0]][current_location[1]] = True
            u[next_location[0]][next_location[1]] = True
            current_location = next_location
    elif i == "R":
        if current_location[1] + 1 < n:
            next_location = [current_location[0], current_location[1] + 1]
            r[current_location[0]][current_location[1]] = True
            r[next_location[0]][next_location[1]] = True
            current_location = next_location
    elif i == "L":
        if current_location[1] - 1 >= 0:
            next_location = [current_location[0], current_location[1] - 1]
            l[current_location[0]][current_location[1]] = True
            l[next_location[0]][next_location[1]] = True
            current_location = next_location

for x in range(n):
    for y in range(n):
        if (d[x][y] or u[x][y]) and (l[x][y] or r[x][y]):
            board[x][y] = '+'
        elif (d[x][y] or u[x][y]):
            board[x][y] = '|'
        elif (l[x][y] or r[x][y]):
            board[x][y] = '-'

for row in board:
    print("".join(row))  # 2차원 배열 출력
