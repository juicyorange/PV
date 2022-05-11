from copy import deepcopy
max_sheep = 0


def dfs(start, visited, wolf_count, info, graph, sheep_count):
    global max_sheep

    if start in visited:
        return

    if info[start] == 1:
        print(start, wolf_count)
        wolf_count += 1
    else:
        sheep_count += 1
        max_sheep = max(max_sheep, sheep_count)

    if(sheep_count <= wolf_count):
        return
    visited.append(start)
    for k in visited:
        for node in graph[k]:
            if node not in visited:
                dfs(node, deepcopy(visited), wolf_count, info, graph, sheep_count)


def solution(info, edges):
    answer = 0

    graph = [[] for _ in range(len(info))]
    for i in edges:
        a = i[0]
        b = i[1]
        graph[a].append(b)
        graph[b].append(a)

    dfs(0, [], 0, info, graph, 0)
    answer = max_sheep
    return answer


print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [
      1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
