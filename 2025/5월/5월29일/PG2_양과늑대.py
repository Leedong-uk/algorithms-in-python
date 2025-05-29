from collections import defaultdict

def solution(info, edges):
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)

    max_sheep = 0

    def dfs(curr, sheep, wolf, next_nodes):
        nonlocal max_sheep

        if info[curr] == 0:
            sheep += 1
        else:
            wolf += 1

        if wolf >= sheep:
            return

        max_sheep = max(max_sheep, sheep)

        # 현재 노드에서 이동 가능한 노드 갱신
        #현재 curr 에서 갈수 있는 모든거 ()= graph[curr])를 다음 방문지 next_node 에 추가
        new_next = next_nodes + graph[curr]
        # 현재 노드를 방문했으므로 제외
        if curr in new_next:
            new_next.remove(curr)

        for i in range(len(new_next)):
            dfs(new_next[i], sheep, wolf, new_next[:i] + new_next[i+1:])

    dfs(0, 0, 0, [])
    return max_sheep
