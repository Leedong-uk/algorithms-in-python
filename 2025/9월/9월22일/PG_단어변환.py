from collections import deque , defaultdict
def solution(begin,target,words) : 
    answer = 0 
    linked_list = defaultdict(list)
    visited = defaultdict(int)
    q = deque()

    words = [begin] + words

    def get_next_node (word1,word2) : 
        cnt = 0
        for x,y in zip(word1,word2) : 
            if x != y : 
                cnt +=1
        return cnt == 1 
    
    for i in range(len(words)) : 
        for j in range(len(words)) : 
            if words[i] == words[j] : 
                continue 
            else : 
                if get_next_node(words[i],words[j]) : 
                    linked_list[words[i]].append(words[j])
                    # linked_list[words[j]].append(words[i])
    
    for word in words : 
        visited[word] = -1 
    
    visited[begin] = 0 
    q.append(begin)

    while q : 
        node = q.popleft()

        for next_node in linked_list[node] : 
            if visited[next_node] == -1 : 
                visited[next_node] = visited[node] + 1
                q.append(next_node)
    
    if visited[target] != -1 : 
        return visited[target]
    else : 
        return 0
    
print(solution("hit","cog",["hot","dot","dog","lot","log","cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))

