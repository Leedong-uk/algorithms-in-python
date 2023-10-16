import sys

n = sys.stdin.readline().rstrip()
stick = []
answer = 0


for i in range(0,len(n)) : 
    if n[i] =="(" : 
        stick.append(n[i])
    

    elif n[i] == ")" : 
        if n[i-1] =="(":
            stick.pop()
            answer = answer + len(stick)
        
        elif n[i-1] == ")" : 
            stick.pop()
            answer = answer + 1

print(answer)

