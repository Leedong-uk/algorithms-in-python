from collections import deque 
# S : 시작지점
# E : 출구
# L : 레버
# O : 통로
# X : 벽
def solution(maps) : 
    answer = 0 
    n = len(maps) 
    m = len(maps[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(n) : 
        for j in range(m) : 
            if maps[i][j] == "S" : 
                start_x,start_y = i,j
            elif maps[i][j] == "L" : 
                lever_x,lever_y = i , j 
            elif maps [i][j] == "E" : 
                exit_x , exit_y = i,j
    


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))