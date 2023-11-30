#이제까지 bfs는 가중치가 1일떄 최단거리를 구할수 있다고 알고있었음
#근데 사실 가중치가 0과 1일떄 에도 최단거리를 구할수있다
#bfs에서 큐를 보면 시작점 거리1인애들 거리2인애들 ... 이런식으로 되어있다
#이걸 큐를 다 쪼개는거다 즉 거리가 0인큐 거리가 1인큐 거리가 3인큐.....
#그래서 거리가 0인큐에 있는 모든 애들을 다 처리후 거리가 1인큐로 넘어가고 거기 애들 기준으로 가중치가 0이면 거리가 1인거니까
#그런애들 추가해줄거 추가해주고 또 거기기준 가중치가 1이면 거리가 2인소리니깐 거리가 2인 큐에 추가해주고..
#이런식으로 현재큐와 다음큐 단 2개의 큐만으로도 최단거리를 구할수있다
#근데 이것도 좋은데 덱을 이용하면 덱 하나만으로 다 처리할수있다
#어떻게하냐면 덱 의 앞부분에는 현재 queue에 넣어야할것 즉 현재를 기준으로 가중치가 0인애들을 넣어주고
#덱의 뒷부분에는 현재queue을 기준으로 가중치가 1인애들을 넣어준다
#당연히 처리는 덱의 앞부분부터 하면된다

from collections import deque
MAX = 200000 
check = [False]*MAX
dist = [-1]*MAX
start , end = map(int,input().split())
check[start] = True
dist[start] = 0 
q = deque()
q.append(start)

while q : 
    now = q.popleft()
    if now*2 < MAX and check[now*2] == False : 
        q.appendleft(now*2)
        check[now*2] = True
        dist[now*2] = dist[now]

    if now-1 >=0 and check[now-1] == False : 
        q.append(now-1)
        check[now-1] = True
        dist[now-1] = dist[now] +1

    if now+1 < MAX and check[now+1] == False : 
        q.append(now+1)
        check[now+1] = True
        dist[now+1] = dist[now]+1

print(dist[end])
