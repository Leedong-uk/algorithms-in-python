n = input()
answer = [0] * 26

for i in n : 
    answer[ord(i)-97] +=1


print(" ".join(list(map(str,answer))))