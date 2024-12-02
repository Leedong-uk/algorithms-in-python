N = int(input())
bo = [list(input()) for _ in range(N)] 
maxcnt = 0



def check() : 
    global maxcnt
    for i in range(N) : 
        cnt = 1
        for j in range(1,N):
            if bo[i][j] == bo[i][j-1]:
                cnt+=1
                maxcnt = max(cnt,maxcnt)
            else:
                cnt = 1

        cnt =1
        for j in range(1,N) : 
            
            if bo[j][i] == bo[j-1][i] : 
                cnt +=1
                maxcnt = max(cnt,maxcnt)
            else:
                cnt = 1

                







for i in range(N) : 
    for j in range(N) : 
        if j+1 < N:
            bo[i][j],bo[i][j+1] = bo[i][j+1],bo[i][j]
            check()
            bo[i][j],bo[i][j+1] = bo[i][j+1],bo[i][j]
        
        if i+1 < N : 
            bo[i][j],bo[i+1][j] = bo[i+1][j],bo[i][j]
            check()
            bo[i][j],bo[i+1][j] = bo[i+1][j],bo[i][j]

       

print(maxcnt)
