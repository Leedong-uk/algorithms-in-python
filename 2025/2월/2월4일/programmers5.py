direction={"E":[0,1],"W":[0,-1],"N":[-1,0],"S":[1,0]}
result = []
park_matrix = [list(i) for i in park]
start =[0]*2
routes = ["E 2","S 2","W 1"]
park = ["SOO","OOO","OOO"]

    #시작점 찾기
for i in range(len(park_matrix)) : 
    for j in range(len(park_matrix[i])) :
        if park_matrix[i][j] =='S' : 
            start = [i,j]
            break

for i in routes : 
    key, value = i.split()
    value = int(value)

    for _ in value :
        dx , dy = start[0]+direction[key][0] , start[1]+direction[key][1]
        if 0<=dx<len(park_matrix) and 0<=dy<len(park_matrix[0]) : 
            if park_matrix[dx][dy] == 'X' : 
                break
            else : 
                start = [dx,dy]
        else : 
            break