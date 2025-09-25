from collections import deque , defaultdict
def solution(begin,target,words) : 
    answer = 0 
    linked_list = defaultdict(list)
    visited_list = defaultdict(int)
    words = [begin] + words
    for word in words : 
        visited_list[word] = -1
   
    q = deque()

    def get_next_node(word1,word2) : 
        cnt = 0
        for x , y in zip(word1,word2) : 
            if x !=y : 
                cnt +=1 
        
        return cnt == 1 
    
    for i in range(len(words)) : 
        for j in range(len(words)) : 
            if words[i] == words[j] : 
                continue 
            if get_next_node(words[i],words[j]) : 
                linked_list[words[i]].append(words[j])
    
    visited_list[begin] = 0
    q.append(begin)

    while q :
        x = q.popleft()

        for next_node in linked_list[x] : 
            if visited_list[next_node] == -1 : 
                visited_list[next_node] = visited_list[x] + 1
                q.append(next_node)
    
    if visited_list[target] != -1 : 
        return visited_list[target]
    else : 
        return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",	["hot", "dot", "dog", "lot", "log"] ))