n = int(input())
x = []
for i in range(n) : 
    num = int(input())
    x.append(num)

x.sort()

for i in range(len(x)) :
    print(x[i])