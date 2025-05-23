queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

total_val = sum(queue1) + sum(queue2) 

if total_val %2 != 0 :
    print(-1)
target = total_val // 2 
max_count = len(queue1) * 3
count = 0

while count <= max_count : 
    sum1 = sum(queue1)
    if sum1 == target : 
        print(count)
    
    elif sum1 > target : 
        x = queue1.pop(0)
        sum1 -= x
        queue2.append(x)
    else : 
        x = queue2.pop(0)
        sum1 +=x
        queue2.append(x)
    
    count+=1




