k = int(input())
moon = list(map(str,input().split()))
tmp = []
check = [False]*(11)
ans = [0]*(k+1)

#m_check 
def m_check(ans) : 

    for i in range(k) : 
        if moon[i] == '<' : 
            if  ans[i] > ans[i+1] : 
                return False
    
        elif moon[i] == '>' : 
            if  ans[i] < ans[i+1] :
                return False
    
    return True
    
        
#go
def go (index,n) : 
    if index == n+1 :
        if m_check(ans) : 
            x= "".join(map(str,ans))
            tmp.append(x)
            return
        return

    for i in range(10) : 
        if check[i] : 
            continue

        check[i] = True 
        ans[index] = i
        go(index+1,n)
        check[i] = False 

go(0,k)
tmp.sort()
print((tmp[-1]))
print((tmp[0]))
