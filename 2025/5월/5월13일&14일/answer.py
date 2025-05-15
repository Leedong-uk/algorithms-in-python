from collections import deque

def solution(board):
    n = len(board)
    visited = set()
    q = deque()
    q.append(((0, 0), (0, 1), 0))  # (좌표1, 좌표2, 시간)
    visited.add(((0, 0), (0, 1)))

    def can_move(pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return 0 <= x1 < n and 0 <= y1 < n and \
               0 <= x2 < n and 0 <= y2 < n and \
               board[x1][y1] == 0 and board[x2][y2] == 0

    while q:
        pos1, pos2, cost = q.popleft()
        if pos1 == (n-1, n-1) or pos2 == (n-1, n-1):
            return cost

        # 이동
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            np1 = (pos1[0]+dx, pos1[1]+dy)
            np2 = (pos2[0]+dx, pos2[1]+dy)
            if can_move(np1, np2) and (np1, np2) not in visited:
                visited.add((np1, np2))
                q.append((np1, np2, cost+1))

        # 회전
        x1, y1 = pos1
        x2, y2 = pos2
        if x1 == x2:  # 가로 방향이면
            for d in [-1, 1]:
                if 0 <= x1 + d < n and board[x1 + d][y1] == 0 and board[x2 + d][y2] == 0:
                    if ((x1, y1), (x1 + d, y1)) not in visited:
                        visited.add(((x1, y1), (x1 + d, y1)))
                        q.append(((x1, y1), (x1 + d, y1), cost + 1))
                    if ((x2, y2), (x2 + d, y2)) not in visited:
                        visited.add(((x2, y2), (x2 + d, y2)))
                        q.append(((x2, y2), (x2 + d, y2), cost + 1))
        else:  # 세로 방향이면
            for d in [-1, 1]:
                if 0 <= y1 + d < n and board[x1][y1 + d] == 0 and board[x2][y2 + d] == 0:
                    if ((x1, y1), (x1, y1 + d)) not in visited:
                        visited.add(((x1, y1), (x1, y1 + d)))
                        q.append(((x1, y1), (x1, y1 + d), cost + 1))
                    if ((x2, y2), (x2, y2 + d)) not in visited:
                        visited.add(((x2, y2), (x2, y2 + d)))
                        q.append(((x2, y2), (x2, y2 + d), cost + 1))
