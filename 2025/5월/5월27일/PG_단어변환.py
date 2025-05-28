from collections import deque, defaultdict

def solution(begin,target,words) : 
    answer = 0
    new_words = [begin] + words
    linked_list = defaultdict(list)
    check_list = defaultdict(int)
    
    def compare_word(word1,word2) : 
        diff = 0
        for x,y in zip(word1,word2) : 
            if x!=y : 
                diff+=1
        
        return diff == 1
    
    def make_graph () :  
        n = len(new_words)
        for i in range(n) : 
            for j in range(i,n) : 
                if new_words[i] != new_words[j] and compare_word(new_words[i],new_words[j]):
                    linked_list[new_words[i]].append(new_words[j]) 
                    linked_list[new_words[j]].append(new_words[i])
                    
    def make_check() : 
        for i in new_words : 
            check_list[i] = -1
    
    def bfs() : 
        q = deque()
        check_list[begin] = 0
        q.append(begin)
        while q :
            x = q.popleft()
            value = check_list[x]
            for i in linked_list[x] : 
                if check_list[i] == -1 : 
                    check_list[i] = value+1
                    q.append(i)
                    
    
    def start() : 
        make_graph()
        make_check()
        bfs()
    
    start()
    answer = check_list[target]
    return answer


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
