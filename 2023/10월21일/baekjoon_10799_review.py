import sys

n = sys.stdin.readline().rstrip()
stick = 0
answer = 0

for i in range(len(n)) : 
    if n[i] == "(" : 
        stick+=1
    
    elif n[i] ==")" : 
        if n[i-1] =="(" : 
            stick -=1
            answer +=stick
        
        elif n[i-1] ==")" : 
            stick-=1
            answer +=1

print(answer)


