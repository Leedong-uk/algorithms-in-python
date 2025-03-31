'''
A = 9
C = 8
G = 7
D = 6
E = 5
B = 4
F = 3
-> 정해진게 아니라 주어진 단어롤 보고 어떤 숫자를 배정할지 정해서 최대 값을 구하는것 
-> 단어 길이가 긴 애들 부터 
'''
import sys
input= sys.stdin.readline
n = int(input())
temp = []
compute = {}
number= 9
result = 0

#가중치 계산 
for _ in range(n) : 
    x = input().strip()
    temp.append(list(x))
    length = len(x)
    
    for i in x : 
        if i in compute : 
            compute[i] += 10**(length-1)
            length -=1
        else : 
            compute[i] = 10**(length-1)
            length -=1

#내림 차순 정렬
compute = dict(sorted(compute.items(), key=lambda x: x[1], reverse=True))

#숫자 배정 
for i in compute : 
    compute[i] = number
    number -=1

#문자열->숫자 변환 후 합계 계산 

for word in temp : 
    num_str = int(''.join(str(compute[ch]) for ch in word))
    result +=num_str

print(result)
        
        