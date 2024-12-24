n = 3
words=	["hello", "one", "even", "never", "now", "world", "draw"]
check = {}
temp = 0
result = []
stop = False

for i in range(1,len(words)) : 
    if (words[i][0] != words[i-1][-1]) or (words[i] in words[:i]) : 
        return [i%m+1,i//n+1]
    return[0,0]

