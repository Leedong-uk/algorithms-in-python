from collections import deque
import sys

d = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(0,n) : 
    cmd = sys.stdin.readline().split()

    #push_fornt
    if cmd[0] == "push_front" : 
        d.appendleft(cmd[1])
    
    #push_back
    elif cmd[0]=="push_back" : 
        d.append(cmd[1])

    #push_front
    elif cmd[0] == "pop_front" : 
        if d : 
            print(d.popleft())
        else :
            print("-1")
    
    #pop_back
    elif cmd[0] == "pop_back" : 
        if d : 
            print(d.pop())
        else : 
            print("-1")

    #size
    elif cmd[0] == "size" : 
        print(len(d))

    #empty
    elif cmd[0] == "empty" : 
        if d :
            print("0")
        else:
            print("1")

    elif cmd[0] == "front" : 
        if d:
            print(d[0])
        else:
            print("-1")

    elif cmd[0] == "back" :
        if d:
            print(d[len(d)-1])
        else : 
            print("-1")    

