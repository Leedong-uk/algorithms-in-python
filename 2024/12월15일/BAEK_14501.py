n = int(input())
T=[]
P=[]
result = []
day = 0
money = 0
Index = 0
for i in range(n) : 
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

for i in range(n) : 
    Index = i
    money = 0
    day = 0
    while True : 
            if (Index+1) + T[Index] > n : 
                if (Index+1) + T[Index] == n+1 :
                    money += P[Index]

                result.append(money)
                break
            else : 
                day = (Index+1) + T[Index] 
                money += P[Index]
                Index = Index+T[Index]

print(result)
