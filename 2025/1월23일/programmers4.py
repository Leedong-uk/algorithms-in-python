order = [3, 5, 4, 2, 1]
total = len(order)
sub = []
answer = 0 
i = 1
while  i<= total:
    if order and  order[0] == i : 
        order.pop(0)
        answer +=1
        
    elif sub and order and order[0] == sub[-1] :
        sub.pop(-1)
        order.pop(0)
        answer +=1
    else : 
        sub.append(i)
    print('i : ',i)
    print('stack : ',sub)
    print('order : ',order)
    i +=1

while sub and order and  sub[-1] == order[0] :
    sub.pop(-1)
    order.pop(0)
    answer +=1

print(answer)