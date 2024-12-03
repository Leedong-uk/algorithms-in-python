n, m = map(int, input().split())
left = 0
right = m - 1
k = int(input())
box = [False for _ in range(n)]
distance = 0

for i in range(m):
    box[i] = True

for i in range(k):
    apple = int(input()) - 1
    if box[apple] == False:
        for j in range(left, right + 1): 
            box[j] = False
        move = min(abs(apple - left), abs(apple - right))
        if apple > right :
            left += move
            right += move
        elif apple < left :
            left -= move
            right -= move

        if 0 <= left < n and 0 <= right < n:
            for j in range(left, right + 1):  
                box[j] = True
            distance += move
        else:
            left -= move
            right -= move

print(distance)
