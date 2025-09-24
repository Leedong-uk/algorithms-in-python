from collections import deque
def solution(places) : 
    answer = []
    for place in places : 
        for i in range(5) : 
            for j in range(5) : 
                if place[i][j] == "P" : 
                    if not dfs(i,j,place) : 
                        answer.append(0)
                else : 
                    answer.append(1)
        
    return answer

def dfs(start_x,start_y,place) : 
    q = deque()
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    check = [[False]*5 for _ in range(5)]
    
    q.append((start_x,start_y,0))
    check[start_x][start_y] = True
    
    while q : 
        x,y,dist = q.popleft()
        
        if dist >=1 and place[nx][ny] == "P" : 
            return False
        if dist == 2 : 
            continue 
        
        for k in range(4) : 
            nx , ny = x+dx[k] , y+dy[k]
            if 0 <= nx < 5 and 0 <= ny < 5 : 
                if place[nx][ny] != "X" and check[nx][ny] == False : 
                    dist +=1
                    q.append((nx,ny,dist))
    return True 
            
    


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

