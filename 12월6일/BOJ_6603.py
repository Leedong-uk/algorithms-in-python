def go(index,start ,n, m):
    if index == m:
        tmp.append(tuple(ans))
        return
    
    for i in range(start,n):
        if check[i]:
            continue
        check[i] = True
        ans[index] = num[i]
        go(index+1,i, n, m)
        check[i] = False




while True : 
    num = list(map(int,input().split()))
    if len(num) == 1 and num[0] == 0 :
        break
    num = num[1:]
    n = len(num)
    check = [False]*n
    ans = [0]*6
    tmp = []

    go(0,0,n,6)
    tmp.sort()

    for i in tmp: 
        print(" ".join(map(str,i)))

    print(" ")