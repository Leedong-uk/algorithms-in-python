lottos = [45, 4, 35, 20, 3, 9]
win_nums =[20, 9, 3, 45, 4, 35]
score = 0
rest = 0
rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}

for i in lottos : 
    if i in win_nums :
        score +=1
    if i == 0 :
        rest +=1

print('max rank :',rank[score+rest])
print('min rank :',rank[score])