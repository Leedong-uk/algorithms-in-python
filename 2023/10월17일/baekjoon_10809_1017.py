n = input()
answer = [-1]*26
x = 0


for i in n : 
    if 97<= ord(i) <= 122 :
        if answer [ord(i)-97] == -1 : 
            answer[ord(i)-97] = x
            x += 1 
        else : 
            x += 1 

print(" ".join(list(map(str,answer))))