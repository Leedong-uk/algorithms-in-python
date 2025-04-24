n = int(input())
board = list(map(int,input().split()))

max_honey = max(board)
temp = board.count(max_honey)


print(temp)