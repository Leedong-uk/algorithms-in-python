num = list(map(int,input().split()))

def check_asc (num):
    check = True
    for i in range(len(num)) :
        if num[i] == i+1 :
            check = True
        else : 
            check  = False
            break  
    return check

def check_desc (num):
    check = True
    for i in range(len(num)) :
        if num[i] == 8-i :
            check = True
        else : 
            check  = False
            break
    return check

if check_asc(num) :
    print('ascending')
elif check_desc(num) : 
    print('descending')
else:
    print('mixed')