# 빨,파,노,녹 1~9 = 36장  이중에서 5장 
# 1. 5장이 모두 같은색이면서 숫자가 연속적일떄 -> 가장 높은 숫자에 900을 더함  
# 2. 5장중 4장의 숫자가 같을땐 숫자에 800을 더함 
# 3. 5장중 3장의 숫자가 같고 나머지 2장도 숫자가 같을떄 3장이 같은숫자에 10 을곱하고 2장이 같은 숫자에 더한다음 700을 더함
# 4. 5장의 카드 색깔이 모두 같을떈 가장 높은 숫자에 600을 더함
# 5. 5장의 숫자가 연속적일떄 점수는 가장 높은 숫자에 500을 더함
# 6. 카드 5장중 3장의 숫자가 같을 떄 점수는 같은 숫자에 400을 더한다 
# 7. 카드 5장중 2장의 숫자가 같고 또 다른 2장의 숫자가 같을떈 같은숫자중 큰 숫자에 10을 곱하고 같은수중 작은숫자에 더한다음 300을 더함
# 8. 카드 5장중 2장의 숫자가 같을떄 점수는 같은 숫자에 200을 더함
# 9. 위의 어떤 경우에도 해당 안되면 가장 큰 숫자에 100을 더함 
color_list = [0]*4
number_list = [0]*10
temp = []
data = []
score = 0

for _ in range(5) : 
    color , number = input().split()
    data.append([color,int(number)])
    if color == 'R' : 
        color_list[0] += 1 
    elif color == 'B' : 
        color_list[1] +=1 
    elif color == 'Y' : 
        color_list[2] +=1
    else : 
        color_list[3] +=1
    number_list[int(number)] +=1

color_check = max(color_list) #색깔 반복 횟수
number_check = max(number_list) #숫자 반복횟수
max_number = max(map(lambda x: x[1],data)) #가장 큰 숫자값
min_number = min(map(lambda x: x[1],data)) #가장 작은 숫자값

if color_check == 5 and number_check == 1 : 
    if data[]
    score = max_number + 900


print(score)







    
    

