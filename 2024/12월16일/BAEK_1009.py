n = int(input())
number=[[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

for _ in range(n) : 
    a,b = map(int,input().split())
    a = a%10 
    if a in[1,5,6] : 
        print(a)
    elif a == 0 : 
        print(10)
    else : 
        temp = (b%len(number[a-1]))-1
        print(number[a-1][temp])


