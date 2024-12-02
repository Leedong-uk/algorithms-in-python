import sys

input=sys.stdin.readline
n= int(input())
a=[]
n2 = 0

while True : 
    if n2 == n :
        break
    cmd = input().split()

    if cmd[0] == "push":
        a.append(cmd[1])
    elif cmd[0] == "pop" : 
        if len(a) != 0:
            print(a[len(a)-1])
            del a[len(a)-1]
        else:
            print("-1")
    elif cmd[0] == "size" :
        print(len(a))
    
    elif cmd[0] == "empty" : 
        if len(a)  == 0:
            print("1")
        else:
            print("0")
    elif cmd[0] == "top" :
        if len(a) != 0 :
            print(a[len(a)-1])
        else:
            print("-1")        
          

    n2=n2+1   


