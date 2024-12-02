
n = int(input())
n1 = 0
while True :
    if n1 == n :
        break
    
    n2 = input().split()
    for i in range(0,len(n2)):
        n2[i] = n2[i][::-1]
    result =" ".join(n2)
    print(result)

    n1 =n1+1
     