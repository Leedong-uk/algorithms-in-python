import sys
n = int(sys.stdin.readline().rstrip())
que = []

for _ in range(0,n):
    cmd = sys.stdin.readline().split()

    #push
    if cmd[0] == "push" : 
        que.append(cmd[1])
        
    #pop()
    elif cmd[0] == "pop" :
        if que : 
            print(que.pop(0))
        else : 
            print("-1") 
    
    #size
    elif cmd[0] == "size" : 
        print(len(que))

    #empty
    elif cmd[0] == "empty" : 
        if que : 
            print("0")
        else:
            print("1")

    #front
    elif cmd[0] == "front" :
        if que : 
            print(que[0])
        else : 
            print(-1)          

    #back
    elif cmd[0] == "back" : 
        if que : 
            a= len(que)-1
            print(que[a])
        else:
            print("-1")

            



