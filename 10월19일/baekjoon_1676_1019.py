def factorial (a) : 
    if a == 1 : 
        return 1
    elif a==0 : 
        return 1 
    else: 
        return a*factorial(a-1)
    

n = str(factorial(int(input())))
count = 0 
if n == "1":
    print("0")
else : 
    for i in n[::-1] : 
        if i == "0" :
            count+=1
        else:
            break

    print(count)