food = [1, 7, 1, 2]
temp = ""
for i in range(1,len(food)) :
    temp += str(i)*(food[i]//2)
reverse_temp = temp[::-1]
answer = temp+'0'+reverse_temp
print(answer)