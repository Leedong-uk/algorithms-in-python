n , m = map(int,input().split())

check  = [False] *(n+1)
ans = [0]*m


def go (index,n,m) : 
    if index == m : 
        print(" ".join(map(str,ans)))
        return 
    
    for i in range(1,n+1) : 
        if check[i] : 
            continue
        elif index == 0 :
            check[i] = True
            ans[index] = i
            go(index+1,n,m)
            check[i] = False
            
        elif index !=0 and i > ans[index-1] : 
            check[i] = True
            ans[index] = i
            go (index+1,n,m)
            check[i] = False 


go(0,n,m)