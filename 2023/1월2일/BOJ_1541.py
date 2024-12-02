#마이너스가 나오면 그 뒤에있는 모든 플러스를 괄호로 묵자
#+와 - 를 분리시켜야한다 
#num 에 숫자
#sign 부호
 
s = input().split('-')
num = []

for i in s : 
    sum = 0 
    tmp = i.split("+")
    for j in tmp : 
        sum += int(j)
    num.append(sum)


ans = num[0]

for i in range(1,len(num)) : 
    ans -=num[i]
    

print(ans)
    





