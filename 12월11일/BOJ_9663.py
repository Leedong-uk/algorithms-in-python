def square (x,y) : 
    return (x//3)*3 + (y//3)

def go(z) : #z는 칸수 
    if z == 81 : 
        for i in a : 
            print(' '.join(map(str,i)))
        return True
    
    x = z//n #x행
    y = z%n #y열

    if a[x][y] !=0 : 
        return go(z+1)
    
    else : 
        for i in range(1,10) : 
            if c1[x][i] == False and c2[x][i] == False and c3[square(x,y)][i] == False :
                c1[x][i] == True
                c2[x][i] == True
                c3[square(x,y)][i] == True
                a[x][y] = i
                if go (z+1) : 
                    return True 
                a[x][y] = 0
                c1[x][i] == False
                c2[x][i] == False
                c3[square(x,y)][i] == False
            

n = 9
a = [list(map(int,input().split())) for _ in range(n)]
c1 = [[False]*10 for _ in range(n)] # i행에 숫자 j가 있으면 true
c2 = [[False]*10 for _ in range(n)] # i열에 숫자 j가 있으면 true
c3 = [[False]*10 for _ in range(n)] # i번쨰 블록에 숫자 j 가 있으면 true

for i in range (n) : 
    for j in range (n) : 
        if a[i][j] !=0 : 
            c1[i][a[i][j]] = True
            c2[i][a[i][j]] = True
            c3[square(i,j)][a[i][j]] = True