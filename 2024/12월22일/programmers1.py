wallpaper = ["..", "#."]
temp = []
result = []
# i = 행 j= 열
for i in range(len(wallpaper)) : 
    for j in range(len(wallpaper[i])) :
        if wallpaper[i][j] == '#' : 
            temp.append([i,j])

start_x = min(map(lambda x : x[0],temp))
start_y = min(map(lambda x : x[1],temp))
end_x = max(map(lambda x : x[0],temp)) +1
end_y = max(map(lambda x : x[1],temp)) +1

result = [start_x,start_y,end_x,end_y]
print(result)

