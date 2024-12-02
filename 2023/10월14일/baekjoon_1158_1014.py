import sys
a,b = map(int,sys.stdin.readline().split())

buffer = []
pointer = 0
result = []

buffer = [i for i in range(1,a+1)]

while True : 
    if len(buffer) == 0 : 
        break
        
    pointer = (pointer+(b-1))%len(buffer)

    result.append(str(buffer.pop(pointer)))


print("<"+", ".join(result)+">")



        

        



