import math
n ,a = map(int,input().split())
stack = []
for i in input().split() : 
    stack.append(int(i))

stack_2 = []

for i in stack : 
    stack_2.append(abs(a-i))


while stack_2 and len(stack_2) != 1 : 
    x = math.gcd(stack_2.pop(),stack_2.pop())
    stack_2.append(x)

print(stack_2[0])
