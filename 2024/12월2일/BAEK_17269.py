report = {'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}
n , m = map(int,input().split())
name_1 , name_2 = input().split()
result = []
min_val = min(n,m)
temp = ""

for i in range (min_val) :
    temp += (name_1[i]+name_2[i])

if min_val == n : 
    for i in range(min_val,m) :
        temp += name_2[i]
else:
    for i in range(min_val,n) : 
        temp += name_1[i]

for i in temp : 
    result.append(report[i])

while len(result) != 2 :
    temp2 = []
    for i in range(len(result)) :
        x = (result[i] + result[i-1] ) % 10
        temp2.append(x)
    result= temp2[:]

final = ""
for i in result :
    if i == 0 :
        continue
    final += str(i)
print(final+'%')




ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
import copy
dic = {'A':3,'B':2,'C':1,'D':2,'E':4,'F':3,'G':1,'H':3,'I':1,'J':1,'K':3,'L':1,'M':3,'N':2,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,'U':1,'V':1,'W':1,'X':2,'Y':2,'Z':1}
N, M = map(int, input().split())
A, B = input().split()

min_len = min(N,M)
new = []
for i in range(min_len):
    new += A[i] + B[i]

if N > M:
    new += A[min_len:]
elif N < M:
    new += B[min_len:]

new_num = []
for j in new:
    new_num.append(dic[j])

while len(new_num) > 2:
    temp = []
    for k in range(1, len(new_num)):
        temp_num = new_num[k-1] + new_num[k]
        if temp_num >= 10:
            temp_num -= 10
        temp.append(temp_num)
    new_num = copy.deepcopy(temp)

print("{}%".format(new_num[0]*10 + new_num[1]))
 

