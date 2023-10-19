import sys

num = 1000001
arr = [True for _ in range(num)]
for i in range(2, int((num-1)**0.5)+1):
    if arr[i]:
        for k in range(i*2, num, i):
            arr[k] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    flag = 0

    for a in range(3, len(arr)):
        if arr[a] and arr[n-a] and (a%2 != 0):
            print(str(n) + " = " + str(a) + " + " + str(n-a))
            flag = 1
            break
    if flag == 0:
        print("Goldbach's conjecture is wrong.")

#시간초과가 떴다
#1.처음에는 입력을 받을떄마다 그 수에 맞는 true 수열을 만들었다 그러니깐 매우 비효율적이였음
#2.그래서 반복문 밖에서 한번만 만들어 놓으면 굉장히 효율적일거라 생각했다
#3.시간초과가떠서 인터넷 코드를 봤는데 나랑 똑같았는데 거기선 맞았다되었고 나는 시간 초과가 떴다
#4.이상하게 생각해서 그사람이 맞았다고 생각한 코드를 그대로 복붙해서 제출해봤는데 시간초과가 떴다
#5.흐음...........좀더 생각 해봐야겠다 더 효율적으로 짤수 있는지
    