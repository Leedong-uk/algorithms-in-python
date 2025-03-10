def solution(n):
    # 삼각형 배열 초기화
    triangle = [[0] * (i + 1) for i in range(n)]
    
    num = 1  # 채울 숫자
    row, col = 0, 0  # 시작 위치
    direction = 0  # 0: 아래, 1: 오른쪽, 2: 위로
    
    # 방향 이동을 위한 dx, dy 배열 (아래, 오른쪽, 위로 대각선)
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    for _ in range(n * (n + 1) // 2):  # 총 개수 = 1 + 2 + ... + n = n(n+1)/2
        triangle[row][col] = num
        num += 1

        # 다음 위치 계산
        next_row = row + dr[direction]
        next_col = col + dc[direction]

        # 경계를 벗어나거나 이미 숫자가 채워진 경우 방향 변경
        if not (0 <= next_row < n and 0 <= next_col < len(triangle[next_row]) and triangle[next_row][next_col] == 0):
            direction = (direction + 1) % 3
            next_row = row + dr[direction]
            next_col = col + dc[direction]

        row, col = next_row, next_col

    # 2차원 배열을 1차원 리스트로 변환해서 반환
    return [num for row in triangle for num in row]

# 테스트
print(solution(6))
