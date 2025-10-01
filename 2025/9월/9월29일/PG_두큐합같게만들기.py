from collections import deque 

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1, sum2 = sum(q1), sum(q2)
    total_sum = sum1 + sum2

    if total_sum % 2 != 0:
        return -1
    
    target = total_sum // 2
    max_cnt = (len(q1) + len(q2)) * 2
    cnt = 0

    while cnt <= max_cnt:
        if sum1 == target:
            return cnt
        elif sum1 > target:
            x = q1.popleft()
            sum1 -= x
            sum2 += x
            q2.append(x)
        else:
            x = q2.popleft()
            sum2 -= x
            sum1 += x
            q1.append(x)
        cnt += 1

    return -1

print(solution([3, 2, 7, 2],[4, 6, 5, 1])) 