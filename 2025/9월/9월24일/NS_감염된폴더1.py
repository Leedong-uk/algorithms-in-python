from collections import defaultdict

def solution(folders, p, q):
    answer = None
    linked_list = defaultdict(list)

    # 그래프 만들기
    for x, y in folders:
        linked_list[x].append(y)
        linked_list[y].append(x)

    def dfs(curr, parent):
        nonlocal answer
        found_p = (curr == p)
        found_q = (curr == q)

        for nxt in linked_list[curr]:
            if nxt != parent:
                sub_p, sub_q = dfs(nxt, curr)
                found_p = found_p or sub_p
                found_q = found_q or sub_q

        if found_p and found_q and answer is None:
            answer = curr
        return found_p, found_q

    dfs("root", None)
    return answer


print(solution(
    [["root", "media"], ["media", "images"], ["media", "videos"],
     ["images", "holiday"], ["videos", "concert"]],
    "holiday", "concert"
))
