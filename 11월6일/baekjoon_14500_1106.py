n,m = map(int,input().split())

board=[list(map(int,input().split())) for _ in range(n)]
ans = 0


for i in range(n) : 
    for j in range(m) :
    
    #1번
        if i +3 < n : 
           x = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
           if ans < x  : 
               ans = x
    #2번 
        if j + 3 < m : 
            x = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
            if ans < x : 
                ans = x
    #3번
        if i+1 < n and j+1 < m : 
            x = board[i][j] + board[i+1][j] + board[i][j+1] +board[i+1][j+1]
            if ans < x : 
                ans = x
    
    #4번
        if i+2 < n and j+1 < m : 
            x = board[i][j] + board[i+1][j]+board[i+2][j] + board[i+2][j+1]
            if ans < x : 
                ans = x
    
    #5번
        if i+2 < n and j-1 >= 0 : 
            x = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+2][j-1]
            if ans < x : 
                ans = x
    
    #6번 
        if i+1 < n and j+2 <m: 
            x = board[i][j+2]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
            if ans < x :
                ans = x
    
    #7번
        if i+1 < n and j+2 <m : 
            x = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+2]
            if ans < x :
                ans = x
    
    #8번
        if i+2 < n and j+1 < m : 
            x = board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1]
            if ans < x:
                ans = x
    
    #9번
        if i+2 < n and j+1 < m : 
            x = board[i][j]+board[i+1][j]+board[i+2][j]+board[i][j+1]
            if ans < x:
                ans = x

    #10번
        if i+1 < n and j+2 < m :
            x = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j]
            if ans < x:
                ans = x

    #11번
        if i+1 < n and j+2 < m : 
            x = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
            if ans < x:
                ans = x
    
    #12번
        if i+2 < n and j+1 < m : 
            x = board[i][j]+board[i+1][j]+board[i+1][j+1]+board[i+2][j+1]
            if ans < x:
                ans = x

    #13번
        if i+2 < n and j+1 < m : 
            x = board[i][j+1]+board[i+1][j]+board[i+1][j+1]+board[i+2][j]
            if ans < x:
                ans = x
    
    #14번
        if i+1 < n and j+2 < m : 
            x = board[i+1][j]+board[i][j+1]+board[i+1][j+1]+board[i][j+2]
            if ans < x:
                ans = x
    
    #15번
        if i+1 < n and j+2 < m : 
            x = board[i][j]+board[i][j+1]+board[i+1][j+1]+board[i+1][j+2]
            if ans < x:
                ans = x
    
    #16번
        if i+1 < n and j+2 < m : 
            x = board[i][j]+board[i][j+1]+board[i][j+2]+board[i+1][j+1]
            if ans < x:
                ans = x

    #17번
        if i+2 < n and j+1 < m : 
            x = board[i][j]+board[i+1][j]+board[i+2][j]+board[i+1][j+1]
            if ans < x:
                ans = x

    #18번
        if i+2 < n and j+1 < m  : 
            x = board[i+1][j]+board[i][j+1]+board[i+1][j+1]+board[i+2][j+1]
            if ans < x:
                ans = x

    #19번
        if i+1 < n and j+2 < m : 
            x = board[i][j+1]+board[i+1][j]+board[i+1][j+1]+board[i+1][j+2]
            if ans < x:
                ans = x



print(ans)