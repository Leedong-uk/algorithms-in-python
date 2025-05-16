from collections import deque
R , C = map(int,input().split())
board = [list(input())for _ in range(R)]
q = deque
alpha_check = {}
check = [[False]*R for _ in range(C)]


