from collections import deque

n, m, gas = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
car_x, car_y = map(int, input().split())
car_x -= 1
car_y -= 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

person_list = []

for i in range(m):
    p_x, p_y, g_x, g_y = map(int, input().split())
    person_list.append({
        'start': (p_x - 1, p_y - 1),
        'goal': (g_x - 1, g_y - 1),
    })

def check_next_distance(start_x, start_y):
    distance = [[-1]*n for _ in range(n)]  
    check = [[False]*n for _ in range(n)]
    q = deque()
    q.append((start_x, start_y))
    check[start_x][start_y] = True
    distance[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if not check[nx][ny] and board[nx][ny] == 0:
                    check[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

    candidates = []

    for p in person_list:
        dist = distance[p["start"][0]][p["start"][1]]
        if dist != -1:
            p["distance"] = dist
            candidates.append(p)

    if not candidates:
        return None  
    
    candidates.sort(key=lambda p: (p["distance"], p["start"][0], p["start"][1]))
    return candidates[0]


def get_distance (start_x,start_y,goal_x,goal_y) :
    distance = [[-1]*n for _ in range(n)]  
    check = [[False]*n for _ in range(n)]
    q = deque()
    q.append((start_x, start_y))
    check[start_x][start_y] = True
    distance[start_x][start_y] = 0
    
    while q:
        x, y = q.popleft()
        
        if (x,y) == (goal_x,goal_y) : 
            return distance[goal_x][goal_y]

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if not check[nx][ny] and board[nx][ny] == 0:
                    check[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
    
while person_list:
   
    next_person = check_next_distance(car_x, car_y)
    
    if next_person is None or gas < next_person["distance"]:
        print(-1)
        exit()
    
    #승객 위치로 이동
    gas -= next_person["distance"]
    car_x, car_y = next_person["start"]

    # 승객 목적지까지 이동
    to_goal = get_distance(car_x, car_y, next_person["goal"][0], next_person["goal"][1])
    
    if to_goal == -1 or gas < to_goal:
        print(-1)
        exit()

    gas -= to_goal
    gas += to_goal * 2
    car_x, car_y = next_person["goal"]

    # 완료된 승객 제거
    person_list.remove(next_person)


print(gas)



