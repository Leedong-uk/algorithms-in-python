def solution(folders, p, q):
    linked_list = {}

    for a, b in folders:
        if a not in linked_list:
            linked_list[a] = []
        if b not in linked_list:
            linked_list[b] = []
        linked_list[a].append(b)
        linked_list[b].append(a)

    def dfs(curr, p, q, parent):
        if curr == p or curr == q:
            return curr

        found = []

        for neighbor in linked_list[curr]:
            if neighbor == parent:
                continue
            tmp = dfs(neighbor, p, q, curr)
            if tmp:
                found.append(tmp)

        if len(found) == 2:
            return curr
        elif len(found) == 1:
            return found[0]
        else:
            return None

    return dfs("root", p, q, None)
