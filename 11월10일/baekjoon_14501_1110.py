n = int(input())
T = [0] * (n)
P = [0] * (n)
time = 0

for i in range(n) : 
    T[i],P[i] = map(int,input().split())

ans = 0 
def go (day ,sum) : 
    global ans
    if day == n : 
        ans = max(sum,ans)
        return
    
    if day >n : 
        return
    
    
    go(day+1,sum) #선택안함
    go(day+T[day],sum+P[day]) #선택함


go(0,0)
print(ans)
        
