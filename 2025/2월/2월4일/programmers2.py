#시작점은 #가 있는것중 가장 min
#끝나는 점은 #가 있는것중 가장 max
wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
temp = []
n = len(wallpaper)
m = len (wallpapaer[0])

for i in n : 
    for j in m : 
        if wallpaper[i][j] == '#':
            temp.append([i,j])

start_i = min(map(lambda x : x[0],temp))
start_j = min(map(lambda x : x[1],temp))
end_i = max(map(lambda x : x[0],temp)) +1
end_j = max(map(lambda x : x[1],temp)) +1

answer = [start_i,start_j,end_i,end_j]
