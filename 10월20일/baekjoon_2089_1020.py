"""m = 0
n = 0
x = int(input())
result = []
final = ""

if x == 1 : 
    print("1")

else:
    while True :
        if x == 1 :
            result.append(1)
            break
         
        m = x//-2
        n = x%-2
        x = m
        
    

        if n ==-1 : 
            n =1
            x += 1
            result.append(n)

        elif n ==1 or n == 0 : 
            result.append(n)

        

   
    for i in result[::-1] : 
        final +=str(i)


    print(final)
   """

#모르는 개념이였음 아직도 천천히 하지 않으면 헷갈림..

n = int(input())
res =''
if n == 0:
    print(0)
    exit()
while n:
    if n % (-2):
    
        res = '1' + res
        # -2로 나누어 떨어지지 않는 경우 몫을 구하기 위해 1을 더함
        n = n//-2 + 1
    else:
        res = '0' + res
        n = n//-2

print(res)