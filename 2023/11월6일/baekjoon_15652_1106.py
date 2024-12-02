n , m = map(int,input().split())


ans = [0]*m 


def go (index,n,m) : 
    if index == m : 
        print(" ".join(map(str,ans)))
        return 
    
    for i in range(1,n+1) : 
        if index == 0 : 
            ans[index] = i
            go(index+1,n,m)
        elif i >= ans[index-1] : 
            ans[index] = i
            go(index+1,n,m)

go(0,n,m)