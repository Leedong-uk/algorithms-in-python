I = int(input())
n = I // 5  

while n >= 0:  
    remainder = I - (5 * n)  
    if remainder % 2 == 0:  
        print(n + (remainder // 2))  
        break  
    n -= 1  
else:
    print(-1)  # 5원과 2원으로 정확히 나눌 수 없는 경우


## 그리디 기초문제
