import sys
L_list= list(sys.stdin.readline().rstrip())
R_list = []

for _ in range(int(input())) : 
    cmd = list(sys.stdin.readline().split())
    
    if cmd[0] == "L" and L_list :           #여기서L_list가 비어있는지 아닌지 검사했음
        R_list.append(L_list.pop())

    elif cmd[0] =="D" and R_list : 
        L_list.append(R_list.pop())
    
    elif cmd[0] =="B" and L_list: 
        L_list.pop()
    
    elif cmd[0] == "P" : 
        L_list.append(cmd[1])


answer = L_list + R_list[::-1]  # 여기서 R_list 뒤집어서 합쳐줘야함
print("".join(answer))


