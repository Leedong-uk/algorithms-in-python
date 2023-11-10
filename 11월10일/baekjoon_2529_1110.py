#내일 다시 시도 해 보자!
#범위가 달라서 이전에 했던 방식으로는 힘듬
#일단 손코드를 해보면서 왜 2로 시작하는 애들은 tmp에 저장이 안되었는지
#그리고 그걸 확인했으면 n과 m 방식으로 다시 풀어보자 
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
    
    
    go(index+1,n+1,s+str(index))
    print("index : %d"%index)
    print("s = ",end= " ")
    print(s)
    go(index+1,n,s)


go(1,0,"")
print(tmp)
print(max(tmp))
print(min(tmp))
        