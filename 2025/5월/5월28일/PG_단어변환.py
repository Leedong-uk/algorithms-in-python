from collections import deque, defaultdict

def solution(begin, target, words):
    if target not in words:
        return 0

    new_words = [begin] + words
    linked_list = defaultdict(list)
    check_list = defaultdict(int)

    def compare_word(word1, word2):
        diff = 0
        for x, y in zip(word1, word2):
            if x != y:
                diff += 1
        return diff == 1

    def make_graph():
        n = len(new_words)
        for i in range(n):
            for j in range(i, n):
                if new_words[i] != new_words[j] and compare_word(new_words[i], new_words[j]):
                    linked_list[new_words[i]].append(new_words[j])
                    linked_list[new_words[j]].append(new_words[i])

    def make_check():
        for word in new_words:
            check_list[word] = -1

    def bfs():
        q = deque()
        check_list[begin] = 0
        q.append(begin)

        while q:
            x = q.popleft()
            value = check_list[x]

            for k in linked_list[x]:  
                if check_list[k] == -1:
                    check_list[k] = value + 1
                    q.append(k)

    def start():
        make_graph()
        make_check()
        bfs()

    start()
    answer = check_list[target]
    return 0 if answer == -1 else answer


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))