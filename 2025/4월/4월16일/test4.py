progresses = [93, 30, 55]
speeds = [1, 30, 5]
result = []

while progresses:
    for i in range(len(progresses)):
        progresses[i] += speeds[i]
    if progresses[0] >= 100:
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0) 
            cnt += 1
        result.append(cnt)

print(result) 
