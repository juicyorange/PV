min_intensity = 0
min_summit = 0


def solution(n, paths, gates, summits):
    answer = []
    graph = [[-1 for _ in range(n+1)] for _ in range(len(n+1))]
    for i in paths:
        graph[i[0]][i[1]] = i[2]
        graph[i[1]][i[0]] = i[2]

    for i in gates:

        dfs(i, visited, graph, summits)
    return answer


def dfs(start, visited, graph, summits):
    global min_intensity

    if start in visited:
        return
    visited.append(start)
    for k in visited:
        for node in graph[k]:
            if node not in visited:
                dfs(node, visited, graph, summits)


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [
         3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
