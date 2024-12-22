park = ["OSO","OOO","OXO","OOO"]
park_matrix = [list(i) for i in park]
routes = ["E 2","S 3","W 1"]
result = []
direction={"E":[0,1],"W":[0,-1],"N":[-1.0],"S":[1,0]}
start =[0]*2

#시작점 찾기
for i in range(len(park_matrix)) : 
    for j in range(len(park_matrix[i])) : 
        if park_matrix[i][j] =='S' : 
            start = [i,j]
            break

#direction 만들기
for i in routes : 
    key,value = i.split(" ")
    value = int(value)
    check = False
    pre = [start[0],start[1]]
    for j in range(value) : 
        dx , dy = start[0] + direction[key][0] , start[1] +direction[key][1]
        if 0<=dx<len(park_matrix) and 0<=dy<len(park_matrix[0]) : 
            if park_matrix[dx][dy] =='X' : 
                check = True 
                break
            else : 
                start = [dx,dy]
        else :
            check = True
    
    if check :
        start = pre

print(start)








["OXXO", "XSXO", "XXXX"], ["E 1", "S 1"]
 [1, 1]