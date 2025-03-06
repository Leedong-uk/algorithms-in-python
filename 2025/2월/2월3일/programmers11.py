from collections import Counter
x = "5525"
y = "1255"
temp = []
x_count = Counter(x)
y_count = Counter(y)

for i in x_count : 
    if i in y_count : 
        cnt = min(x_count[i],y_count[i]) 
        temp.extend([i]*cnt)

if temp : 
    answer = ''.join(sorted(temp,reverse=True))
else : 
    answer = "-1"
print(answer)