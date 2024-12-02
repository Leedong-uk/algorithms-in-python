ans = list(map(int,input().split()))
i=1
E,S,M = 1,1,1

while True : 
    if ans[0]==1 and ans[1]==1 and ans[2]==1 : 
        print(i)
        break


    if E == ans[0] and S == ans[1] and M == ans[2] : 
        print(i+1)
        break
    
    i+=1

    E = (i%15)+1
    S = (i%28)+1
    M = (i%19)+1
