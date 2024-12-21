from collections import Counter
x="5525"
y = "1255"

x_check = Counter(list(x))
print("x_check : ",x_check)
y_check = Counter(list(y))
print("y_check : ",y_check)
pair = []

for i in x_check : 
    if i in y_check :
        print("공통 숫자 : ",i)
        number = min(x_check[i],y_check[i]) 
        print("공통 숫자 : ",i,"반복횟수 : ",number)
        for _ in range(number) :
            pair.append(i)

pair.sort(reverse = True)

if not pair : 
    print('-1')
    
else : 
    print("".join(pair))
