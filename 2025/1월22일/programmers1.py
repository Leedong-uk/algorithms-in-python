msg = "KAKAO"
dic = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 
    'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 
    'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

msg = list(msg)
answer = []
last_index = 27

while msg:
    start = msg[0]
    temp = ''
    
    for i in range(1, len(msg)):
        temp = start + msg[i]
        
        if temp in dic:
            start = temp 
        else:
            answer.append(dic[start])
            dic[temp] = last_index  
            last_index += 1
            msg = msg[i:]  
            break
    else:
        answer.append(dic[start])
        break

print(answer)
