a , b , c = map(int,input().split())
check = [0 for i in range(101)]

for i in range(3) : 
    start , end = map(int,input().split())
    for j in range(start,end) : 
        check[j] +=1

find_A = check.count(1)
find_B = check.count(2)
find_C = check.count(3)

print((a*find_A) + (b*find_B*2) + (c*find_C*3))
    