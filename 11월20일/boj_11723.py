#비트마스크 연습
import sys
n=20
m = int(sys.stdin.readline())
s = 0

for _ in range(m) : 
    cmd =  sys.stdin.readline().split()

    if cmd[1]  : 
        x = int(cmd[1])-1

    if cmd[0] == "add" : 
        s = (s | (1<<x))
    
    elif cmd[0] == "remove" : 
        s = (s & ~(1<<x))

    elif cmd[0] == "check" : 
        check = (s &(1 << x))
        if check >0 : 
            sys.stdout.write('1\n')
        else : 
            sys.stdout.write('0\n')
    
    elif cmd[0] == "toggle" : 
        s = (s ^ (1<<x))
    
    elif cmd[0] =="all" : 
        s = (1<<n)-1
    
    else : 
        s = 0
    
   
