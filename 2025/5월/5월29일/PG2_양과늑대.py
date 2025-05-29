def solution(info, edges):
    visited = [False] * len(info)
    visited[0] = True  # ✅ 0번 노드를 방문한 상태로 시작

    def dfs(sheep, wolf):
        # ✅ 만약 늑대가 양보다 크거나 같으면 빠져나온다.
        if sheep == wolf:
            return sheep

        max_sheep = sheep

        # ✅ 모든 edge를 확인
        for parent, child in edges:
            # ✅ 부모가 방문된 상태이고 자식이 아직 방문되지 않았다면
            if visited[parent] and not visited[child]:
                visited[child] = True  # 방문 처리

                if info[child] == 0:  # 양
                    max_sheep = max(max_sheep, dfs(sheep + 1, wolf))
                else:  # 늑대
                    max_sheep = max(max_sheep, dfs(sheep, wolf + 1))

                visited[child] = False  # 방문 해제 (백트래킹)

        return max_sheep

    return dfs(1, 0)
