n = 4
k = 2
number = [x for x in range(1, n + 1)]
answer = []
used = [False] * len(number)
def dfs(path, used):
    if len(path) == k:
        answer.append(path)
        return
    for i in range(len(number)):
        if not used[i]:
            used[i] = True
            dfs(path + [number[i]], used)
            used[i] = False

dfs([], used)
print(answer)
