def solution(files):
    answer = []
    files_dic = {}
    
    for i in range(len(files)) :
        files_dic[i] = []
    
    start = None
    end = None
    
    for j in range(len(files)) : 
        check = [False] * len(files[j])
        for i in range(len(files[j])) : 
            check[i] = files[j][i].isdigit()
            
            if i>0 and check[i-1] != check[i] :
                if check[i] : 
                    start = i
                else : 
                    end = i-1
                    break
        else : 
            end = len(files[j]) -1
        
        head = files[j][:start].lower()
        number = files[j][start:end+1]
        tail = files[j][end+1:]
        
        files_dic[j].extend([head,number,tail])
    
    files_dic = dict(sorted(files_dic.items(), key=lambda x: (x[1][0], int(x[1][1])))) 
    
    answer = [files[key] for key in files_dic]
    return answer