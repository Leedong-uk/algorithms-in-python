"""""
n , m = map(int,input().split())

def factorial (a) : 
    if a == 1 : 
        return 1
    elif a == 0 :
        return 1
    else : 
        return a*factorial(a-1)



def combination (n,m) : 
    if n < m or n == 0 : 
        return False
    elif m == 0 :
        return 1
    else : 
        return int(factorial(n) /( factorial(m) * factorial(n-m)))
    

y = str(combination(n,m))
count = 0

for i in y[::-1] : 
    if i =="0" :
        count+=1
    else : 
        break


print(count)
"""""
#위에 코드처럼 단순히 팩토리얼로 구할려고했는데 오류가 났다
#정답률을보니 20% 다들 그렇게 생객했나보다
#인터넷을 검색해봤는데 결국 끝자리가 0임을 새는거니깐 2,5의 쌍을 구하면 0의수를 알수있다
#나머지는 아이패드에 정리해보겠다
#최종적인 값은 팩토리얼 형태가 아니므로, 5의 지수만을 고려해서는 안된다. 
#이 경우에는 2의 지수, 5의 지수를 둘다 구해서 둘 중 작은 값을 답으로 취해야한다. 
#여기서조합에서의  2의 지수 = n!의 2의 지수 - (n-r)!의 2의 지수 - r!의 2의 지수
#                 5의 지수 = n!의 5의 지수 - (n-r)!의 5의 지수 - r!의 5의 지수


import sys
n,m = map(int,input().split())
count = 0

def count_2 (a) : 
    count = 0 
    if a < 2  : 
        return 0
    
    while a>=2 : 
        x = a//2
        count+=x
        a = a//2
    return count

def count_5(a) : 
    count = 0

    if a < 5 : 
        return 0 
    
    while a>=5 : 
        x = a//5
        count +=x
        a = a//5
    return count

two_count = count_2(n) - count_2(n-m) - count_2(m)
five_count = count_5(n) - count_5(n-m) - count_5(m)
print(min(two_count,five_count))
    
