from collections import deque, defaultdict

def solution(begin,target,words) : 
    linked_list = defaultdict(list)
    check = defaultdict(int)
    new_words = [begin] + words
    def compare_word (word1,word2):
        diff = 0
        for x,y in zip (word1,word2) : 
            if x!= y : 
                diff +=1
        
        return diff == 1 
    

    def make_graph () : 
        
        for i in new_words : 
            for j in new_words : 
                if i == j : 
                    continue

                if compare_word(i,j) : 
                    linked_list[i].append(j) 
                    linked_list[j].append(i)
    
    def initialize() : 
        for word in new_words : 
            check[word] =-1
    
    def make_answer (begin,target) : 
        q = deque()
        check[begin] = 0
        q.append(begin)
        
        while q: 
            x = q.popleft()
            value = check[x]

            for i in linked_list[x] : 
                if check[i] == -1 : 
                    check[i] = value+1
                    q.append(i)
    make_graph()
    initialize()
    make_answer(begin,target)
    print(check[target])

solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit","cog",["hot", "dot", "dog", "lot", "log"])

        



            