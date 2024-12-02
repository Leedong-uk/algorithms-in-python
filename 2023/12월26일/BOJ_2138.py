import sys
input = sys.stdin.readline

def change(a,index) :  #항상 바꿀때는 가운대를 기준으로 하네
    for i in range(index-1,index+2) : 
        if 0<= i <len(a) : 
            a[i] = 1-a[i]


def go (a,goal) : #a를 goal로 만들꺼고 , output : (가능여부,스위치 횟수)
    n = len(a)
    ans = 0 
    for i in range(n-1) : 
        if a[i] != goal[i] :
            change(a,i+1)
            ans +=1

    flag = True
    for i in range(n) : 
        if a[i] !=goal[i] : 
            flag = False
    
    if flag : 
        return (True,ans)
    
    else : 
        return(False,ans)
    


n = int(input())
a = list(map(int,input().rstrip()))
goal = list(map(int,input().rstrip()))
b= a[:] #2개를 돌릴꺼기때문에 복사본이 하나 필요함 
p1 = go(b,goal) # 첫번쨰를 안누른경우
change(a,0) 
p2 = go(a,goal) #첫번쨰를 누른경우 

if p2[0] : 
    p2 = (True,p2[1]+1)

if p1[0] and p2[0] : 
    print(min(p1[1],p2[1]))

elif p1[0] : 
    print(p1[1])

elif p2[0] : 
    print(p2[1])

else : 
    print(-1)
