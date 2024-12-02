#단어의 수 
#알파벳 대문자를 0~9 까지의 숫자 중 하나로 바꿔서
#합을구하는 문제 최대치 
#브루트 포스니깐 걍 다 넣고 다 비교하면 되는거 아님??
#넣는 방법을 이제 생각을 해야해 

#abcd 문자열을 만들고 , 배정 안됐으면 false로 뒀다가 큰수부터 하나하나 넣어봐서
#각각의 경우의 결과값을 가지고있다가 최대값을 뽑아내면 되는거아님 ?

import sys

n = int(input())
alphabet_dict = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
alpahbet_list = []
answer = 0
tmp = []


for _ in range(n) :
    alphabet = input()
    tmp.append(alphabet)

for word in tmp : 
    for i in range(len(word)) : 
        num = 10**(len(word)-i-1)
        alphabet_dict[word[i]] += num

for value in alphabet_dict.values() : 
    if value > 0  : 
        alpahbet_list.append(value)

alpahbet_list.sort()
alpahbet_list.reverse()

for i in range(len(alpahbet_list)) : 
    answer += alpahbet_list[i] * (9-i)

print(answer)




