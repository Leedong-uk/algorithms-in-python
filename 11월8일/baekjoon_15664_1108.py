n , m = map(int,input().split())
num = list(map(int,input().split()))
num.sort()

c = [False]*n
ans =[0]*m
tmp = [] 

def go (index,start,n,m): 
    if index == m : 
        tmp.append(tuple(ans))
        return 
    
    for i in range(start,n) : 
        if c[i] : 
            continue

        c[i] = True
        ans[index] = num[i]
        go(index+1,i,n,m)
        c[i] = False 

go(0,0,n,m)

tmp = list(set(tmp))
tmp.sort()
for i in tmp : 
    print(" ".join(map(str,i)))