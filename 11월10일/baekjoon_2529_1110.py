#내일 다시 시도 해 보자!
k = int(input())
moon = list(map(str,input().split()))
s = ""
tmp = []

def go (index,n,s) : 
    if index == k+2 : 
        if n == k+1 : 
            for i in range(k) : 
                x = eval(s[i]+moon[i]+s[i+1])
                if x : 
                    tmp.append(s)
                    return
        
        return
    
    for _ in range(1,10):
        go(index+1,n+1,s+str(index))
        go(index+1,n,s)


go(1,0,s)
print(max(tmp))
print(min(tmp))
        