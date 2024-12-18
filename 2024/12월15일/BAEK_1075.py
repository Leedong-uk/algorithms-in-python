n = int(input())
f = int(input())
n = n//100
n = n*100

for i in range(99) : 
    if (n+i)%f == 0 : 
        if i // 10 == 0 :
            print(format(i,'02'))
            break
        else :
            print(i)
            break
