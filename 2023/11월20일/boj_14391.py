#각 칸이 가로에 속하는지 세로에 속하는지  
#이게 왜가능하냐 최대의 칸의 갯수는 16이고 각 칸은 최대가 16개니깐 최대는 2^16개임
#0번칸부터 15번칸 까지 있을떄 비트마스크로 표현해보자
#가로에 속하면 1 세로에 속하면 0
#오늘은 여기까지 내일다시하장!! 20:00부터
n , m = map(int,input().split())
size = n*m
lst = []
ans = -1 

for _ in range(n) : 
    lst = lst+list(map(int,input()))


for i in range(1<<size) : 
    ga = []
    se = []

    for j in range (size) :
        if (i&(1<<j)) > 0 : 
            ga += [j] 
        
        else : 
            se +=[j]
    print("%d번쨰 케이스 "%i)
    print("가로 : ",end = " ")
    print(ga)
    print("세로 : ",end = " ")
    print(se)
    
    t1 = 0 
    t2 = 0

    if len(ga) != 0 :
        for i in ga : 
            t1 += lst[i]
    print("가로의 합 : %d"%t1)
        

    if len(se) != 0 :
        for i in se : 
            t2 += lst[i]
    print("세로의 합 : %d"%t2)
        
    number = t1+t2
    print("총합 : %d"%number)
    print("-------------------")

    if ans == -1 or ans < number : 
        ans = number


print(ans)


   
