# n = list(input())
# cnt = 0
# result = 0 



# for i in range(len(n)) : 
#     if n[i] == 'O' : 
#         # print("i :",i)
#         for j in range(i,-1,-1) : 
#             if n[j] == 'O' : 
#                 cnt +=1
#             else : 
#                 break
#     result +=cnt
#     cnt = 0 

# print(result)
n = int(input())

for _ in range(n) : 
    m = list(input())
    cnt = 0
    result = 0
    for i in range(len(m)) : 
        if m[i] == 'O' : 
            for j in range(i,-1,-1) : 
                if m[j] == 'O' : 
                    cnt +=1
                else : 
                    break
        result +=cnt
        cnt = 0
    
    print(result)
