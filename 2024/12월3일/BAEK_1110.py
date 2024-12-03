origin_num = int(input())
temp = origin_num
new_right = 0 
new_left = 0
check = 0 


while True :
    if temp < 10 :
        temp = temp*10 + temp
        check +=1
    else : 
        new_left = temp%10
        new_right = ((temp//10) + new_left) % 10
        temp = new_left*10 + new_right
        check +=1
    
    if origin_num == temp :
        break
print(check)

       
