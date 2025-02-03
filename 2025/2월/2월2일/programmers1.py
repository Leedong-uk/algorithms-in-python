def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n): 
        x = format(arr1[i] | arr2[i], 'b').zfill(n)  # n자리 맞추기
        x = x.replace('1', '#').replace('0', ' ')   # 변환
        answer.append(x)
        
    return answer
