n = int(input())
T = [0] *n
P = [0] *n


for i in range(n) : 
    T[i],P[i] = map(int,input().split())

ans = 0
def go(t,p) : 
    global ans 
    if t == n : 
        ans = max(p,ans)
        return

    if t >n :
        return

    go(t+T[t],p+P[t]) #선택하는경우
    go(t+1,p) #선택안하는 경우


go(0,0)
print(ans)

    


#1일날 상담하는경우 상담 안하는경우 