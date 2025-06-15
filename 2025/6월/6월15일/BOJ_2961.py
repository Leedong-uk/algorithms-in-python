n = int(input())
foods = []

for _ in range(n):
    foods.append(list(map(int, input().split())))

def dfs(start, end, depth, score, temp):
    if depth == end:
        sour = 1
        bitter = 0
        for i in temp:
            sour *= foods[i][0]
            bitter += foods[i][1]
        return min(score, abs(sour - bitter))

    for i in range(start, n):
        score = min(score, dfs(i + 1, end, depth + 1, score, temp + [i]))

    return score


min_diff = float('inf')
for i in range(1, n + 1):
    min_diff = min(min_diff, dfs(0, i, 0, min_diff, []))

print(min_diff)
