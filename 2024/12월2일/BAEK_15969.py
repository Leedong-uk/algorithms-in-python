n = int(input())
answer = input()
bonus = 0 
result = 0

for i in range(n) :
    if answer[i] == 'X' :
        bonus = 0 
    else :
        result += i+1
        result += bonus
        bonus +=1

print(result)
