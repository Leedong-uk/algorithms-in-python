a, b = map(int,input().split())
m = int(input())
stack = list(map(int,input().split()))
stack.reverse()
result = []
dec_num = 0


for i in range(m) : 
    
    
    x = stack[i]*(a**i)

    dec_num += x


while dec_num : 
    remain = dec_num % b
    result.append(str(remain))
    dec_num = dec_num//b


result.reverse()

print(" ".join(result))