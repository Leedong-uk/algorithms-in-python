from collections import deque, defaultdict

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
check = {}
linked_list = defaultdict(list)

def word_compare(word1, word2):
    diff = sum([1 for a, b in zip(word1, word2) if a != b])
    return diff == 1

def make_graph():
    all_words = words + [begin]
    for i in all_words:
        for j in all_words:
            if i != j and word_compare(i, j):
                linked_list[i].append(j)
                linked_list[j].append(i)

def initialize() : 
    if begin not in words:
        words.append(begin)

    for i in words:
        check[i] = -1

def bfs(start):
    q = deque()
    check[start] = 0
    q.append(start)

    while q:
        x = q.popleft()
        value = check[x]
        for i in linked_list[x]:
            if check[i] == -1:
                check[i] = value + 1
                q.append(i)

initialize()
make_graph()
bfs(begin)


print(check[target] if check[target] != -1 else 0)
