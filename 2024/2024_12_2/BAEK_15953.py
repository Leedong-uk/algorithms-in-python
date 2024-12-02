n = int(input())

money1 = [0,500,300,300,200,200,200,50,50,50,50,30,30,30,30,30,10,10,10,10,10,10]
money2 = [0,512,256,256,128,128,128,128,64,64,64,64,64,64,64,64,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32]

for i in range(n) : 
    a , b = map(int,input().split())

    if a > 21 : 
        if b > 31 :
            print(0)
        else : 
            print (money2[b]*10000)
    
    if b > 31 and a <= 21 :
        print (money1[a]*10000)

    if  a <=21 and b <= 31 :
        print(money1[a]*10000 + money2[b]*10000)
