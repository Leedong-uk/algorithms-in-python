s="1111111"
check_num = [0]*2
cnt = 0

while s != '1' : 
    check_num[1] = 0
    cnt +=1
    for i in s : 
        if i =='1' : 
            check_num[1] +=1
    
    check_num[0] += len(s)-check_num[1]
    s = format(check_num[1],'b')


print(cnt,check_num[0])