n = 15
end = n//2
cnt = 0

for i in range(1,end+1) : 
    temp = 0
    for j in range(i,end+2) : 
        print("j : ",j)
        temp +=j
        if temp > n :
            print('temp : ',temp,'범위 초과')
            break

        elif temp == n :
            cnt +=1
            break

print(cnt+1)


