n = int(input())  

for _ in range(n):  
    result = 0
    num = int(input())  
    candy = list(map(int, input().split()))  

    for i in range(num):
        if candy[i] % 2 == 1:
            candy[i] += 1

    while min(candy) != max(candy):  
        temp = [c // 2 for c in candy]  
        new_candy = [0] * num  

        # 사탕 분배
        for k in range(num):
            new_candy[k] += candy[k] - temp[k]  # 자신에게 남은 절반
            new_candy[(k + 1) % num] += temp[k]  # 오른쪽 이웃에게 전달

      
        candy = new_candy[:]

       
        for i in range(num):
            if candy[i] % 2 == 1:
                candy[i] += 1

        result += 1  

    print(result)  
