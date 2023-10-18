n = int(input()) 
s = list(input())
stack = []
a= 0

num = [None] * n

for i in range(n) : 
    tmp = input()
    num[i] = tmp


for i in range(len(s)) : 
    if s[i].isalnum() : 
        stack.append(num[a])
       
        if n == 1 :
            pass
        else : 
            a= a+1
    else : 
        if s[i] == "/" : 
            n1 = stack.pop()
            n2 = stack.pop()
            n3 = str(eval(n2+s[i]+n1))
            stack.append(n3)
            
        
        elif s[i] == "-" : 
            n1 = stack.pop()
            n2 = stack.pop()
            n3 = str(abs(eval(n2+s[i]+n1)))
            stack.append(n3)
            
        else : 
            n1 = stack.pop()
            n2 = stack.pop()
            n3 = str(eval(n1+s[i]+n2))
            stack.append(n3)
            


print("%0.2f"%float(stack[0]))



n = int(input())
word = input()
num_list = [0]*n

for i in range(n) : 
        num_list[i] = int(input())

stack = []

for i in word : 
        if i.isalnum() : 
                stack.append(num[i])