n = 16
t = 16
m = 2
p = 1

'''def to_base_n(number, base):  
    if number == 0:
        return '0'
    
    digits = []
    while number: 
        remainder = number % base
        digits.append(str(remainder) if remainder < 10 else chr(remainder - 10 + ord('A')))
        number //= base
        
    return ''.join(digits[::-1])

li = [[] for _ in range(m)]  
check = False
order = 0 
i = 0  


while not check:
    number = to_base_n(i, n) 
    for j in range(len(number)):
        li[order % m].append(number[j])  
        order += 1  

        
        if len(li[p - 1]) == t:
            check = True
            break

    if check:
        break  

    i += 1  

answer = ''.join(li[p - 1])  
print(answer)  '''

n = 16
t = 16
m = 2
p = 1

def to_base_n(number, base):  
    if number == 0:
        return '0'
    
    digits = []
    while number: 
        remainder = number % base
        digits.append(str(remainder) if remainder < 10 else chr(remainder - 10 + ord('A')))
        number //= base
        
    return ''.join(digits[::-1])

game_numbers = ""
i = 0

# 필요한 길이만큼 숫자 생성
while len(game_numbers) < t * m:
    game_numbers += to_base_n(i, n)
    i += 1

# p번째 플레이어의 숫자 추출
answer = ''.join([game_numbers[i] for i in range(p - 1, len(game_numbers), m)][:t])
print(answer)

