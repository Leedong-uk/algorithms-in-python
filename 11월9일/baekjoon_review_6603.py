def go(index, start, n ,m )  : 
    if index == m : 
        tmp.append(tuple(ans)) #현재 ans 에 있는걸 전부를 tuple로 묶어줌
        return
    
    for i in range(start,n) : 
        if c[i] == True : 
            continue

        c[i] == True
        ans[index] = num[i]
        go(index+1,i,n,m)
        c[i] == False

while True : 
    num = list(map(int,input().split()))
    if len(num)==1 and num[0]==0 : 
        break
    num = num[1 : ]
    num = list(set(num))
    num.sort()
    n= len(num)
    m = 6

    c = [False]*n
    ans = [0]*m
    tmp = []


    go(0,0,n,m)
    tmp.sort()

    for i in tmp : 
        print(" ".join(map(str,i)))

    print(" ")