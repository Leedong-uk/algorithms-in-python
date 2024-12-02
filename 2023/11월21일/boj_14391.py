n, m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
ans = 0

for s in range(1<<(n*m)) :  # 모든 부분집합 s 를 다구함 
    sum = 0 
    #가로 : 0 세로 : 1

    #부분집합중 가로로 된것들 계산 시작
    for i in range (n) : 
        cur = 0
        for j in range( m ): 
            k = i*m +j

            if (s & (1<<k)) == 0 : 
                cur  = cur*10 + a [i][j]
            
            else : 
                sum += cur #세로가 나오면 이전까지 cur에 누적된 값을 더함 
                cur = 0
        
        sum += cur    #이번 줄이 끝났을떄 cur에 남아있는 값을 sum에 더함

    #부분집합중 세로로 된것들 계산 시작
    
    for j in range(m) : 
        cur = 0 
        for i in range(n) : 
            k = i*m+j

            if (s&(1<<k)) !=0 : 
                cur = cur*10 +a[i][j]
            
            else : 
                sum += cur
                cur = 0 

        
        sum +=cur


#여기까지하면 부분집합에대한 가로 세로 모두를 sum에 더해서 얻었음
    ans = max(ans,sum) #여기서 최대값 비교

print(ans)

                

