n , m = map(int,input().split())

check = [False]*(n+1)
ans = [0]*(m)

def go(index,n,m) : #index = 현재 숫자를 넣을 자리수  
    if index == m : #n : 숫자의 범위 
        print(" ".join(map(str,ans)))
        return      #m : 순열의 자리수
    
    for i in range(1,n+1) : 
        ans[index] = i
        go(index+1,n,m)
        

go(0,n,m)