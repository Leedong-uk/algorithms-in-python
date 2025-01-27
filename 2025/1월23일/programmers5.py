from collections import deque

def solution(x, y, n):
    # BFS를 위한 큐와 방문 체크 배열 초기화
    q = deque([x])
    check = [-1] * (y + 1)  # 방문 여부와 최소 도달 횟수 저장 (-1: 미방문)
    check[x] = 0  # 시작점 초기화

    # BFS 시작
    while q:
        current = q.popleft()
        current_steps = check[current]

        
        for next_value in [current + n, current * 2, current * 3]:
            if next_value <= y and check[next_value] == -1:
                check[next_value] = current_steps + 1
                q.append(next_value)
    return check[y] if check[y] != -1 else -1 