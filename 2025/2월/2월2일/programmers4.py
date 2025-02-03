number = 5
limit = 3
power = 2
result = 0 

temp = [] 

def find_power (n) : 
    answer = 0
    for i in range(1,int(n**0.5)+1) : 
        if n % i == 0 :
            answer +=1
            if (i**2) != n :
                answer +=1
    return answer 

for i in range(1,number+1) : 
    x =find_power(i)
    if x > limit : 
        x = power
    
    result +=x

print(result)