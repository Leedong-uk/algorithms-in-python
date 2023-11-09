"""def go(index,start ,n, m):
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
    num = list(set(num))
    n = len(num)
    m = 6
    num.sort()
    check = [False]*n
    ans = [0]*m
    tmp = []

    go(0,0,n,m)
    tmp.sort()

    for i in tmp: 
        print(" ".join(map(str,i)))

    print(" ")"""
    
import itertools

while True:

    array = list(map(int, input().split()))

    k = array[0]
    S = array[1:]

    for i in itertools.combinations(S, 6):
        print(" ".join(map(str,i)))

    if k == 0 and len(array)==1:
        exit()
    print()