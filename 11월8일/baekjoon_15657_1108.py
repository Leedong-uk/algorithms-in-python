n , m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

c = [False]*n
ans = [0]*m


def go (index,start,n,m) : 
    if index == m : 
        print(" ".join(map(str,ans)))
        return

    for i in range (start,n) : 
        c[i] = True
        ans[index]  = num[i]
        go(index+1,i,n,m)
        c[i] = False


go(0,0,n,m)