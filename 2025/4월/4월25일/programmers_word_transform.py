from collections import deque, defaultdict

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]

def word_compare(word1, word2):
    diff = 0
    for a, b in zip(word1, word2):
        if a != b:
            diff += 1
        if diff > 1:
            return False
    return diff == 1

def create_graph(begin, words):
    temp = [begin] + words
    linked_list = defaultdict(list)
    
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if word_compare(temp[i], temp[j]):
                linked_list[temp[i]].append(temp[j])
                linked_list[temp[j]].append(temp[i])
    
    return linked_list


if target not in words : 
    print(0)
else : 
    
    linked_list = create_graph(begin, words)
    check = {word: -1 for word in words}
    check[begin] = 0
    q = deque([begin])

    while q:
        x = q.popleft()
        if x == target:
            print(check[x])
            break
    
        for name in linked_list[x]:
            if check[name] == -1:  
                check[name] = check[x] + 1
                q.append(name)


    if check[target] == -1:
        print(0)
