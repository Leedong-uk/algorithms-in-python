import sys
n  = sys.stdin.readline().rstrip()
buf = [] 
result = []

for i in range(len(n)) :
    if i == len(n) -1 : 
       result.append(n)
    else : 
        n1 = n[i+1:]
        result.append(n1)

result.sort()
for i in range(len(result)) : 
    print(result[i])