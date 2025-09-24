# N x N 
# M 명의 승객이 목표 
# 0 -> 빈칸 
# 1 -> 벽 


def bfs(start_x,start_y,goal_x,goal_y) : 
    q = deque()
    visited = [[-1]*n for _ in range(n)]
    q.append((start_x,start_y))
    visited[start_x][start_y] = 0 
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    while q : 
        x,y = q.popleft()
        if (x,y) == (goal_x,goal_y) : 
            return visited[x][y]
        for k in range(4) : 
            nx , ny = x + dx[k] , y + dy[k]
            if 0<= nx < n and 0<= ny < n : 
                if visited[nx][ny] == -1 and board[nx][ny] == 0 : 
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return -1
    
def get_next_person(person_list,start_x,start_y) : 
    for person in person_list : 
        person_x,person_y = person["start"]
        person["distance"] = bfs(start_x,start_y,person_x,person_y)
    person_list.sort(key=lambda p: (p["distance"], p["start"][0], p["start"][1]))
    return person_list

def start_taxi(person_list,gas) : 
    #손님 태움 
    next_person = person_list.pop(0)
    print("손님 정보: ",next_person)
    start_x,start_y = next_person["start"]
    goal_x,goal_y = next_person["goal"]
    required_gas = next_person["distance"]
    

    # 손님을 태울 수 있을지 판단
    if required_gas > gas : 
        return -1 
    else : 
        print("현재 gas: ",gas)
        print("손님 한테 갈때 필요한 gas: ",required_gas)
        gas -= required_gas
        print("손님 도착 후 gas:",gas)
    
    #목적지 이동 가능 여부 계산
    required_gas = bfs(start_x,start_y,goal_x,goal_y)
    print("목적지 이동 필요한 gas",required_gas)
    if required_gas > gas : 
        return -1
    else : 
        gas += required_gas
        print("gas: ",gas)
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    return gas

# 메인 
from collections import deque 

n , m , gas = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
start_x , start_y = map(int,input().split())
start_x -=1
start_y -=1
person_list = []

for _ in range(m) : 
    p_x,p_y,g_x,g_y = map(int,input().split())
    person_list.append({"start" : (p_x-1,p_y-1),"goal" : (g_x-1,g_y-1)})

while person_list : 
    person_list = get_next_person(person_list,start_x,start_y)
    gas = start_taxi(person_list,gas)








