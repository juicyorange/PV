from copy import deepcopy
min_road = 999999999


def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    reverse_graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    for road in roads:
        s, e, w = road
        graph[s][e] = w
        reverse_graph[e][s] = w
    visited = [0 for _ in range(n+1)]
    dfs(start, visited, graph,  traps, end, 0)
    answer = min_road
    return answer


def trap_change(graph, cur):
    temp_graph = deepcopy(graph)
    for i in range(len(graph)):
        graph[cur][i] = temp_graph[i][cur]
        graph[i][cur] = temp_graph[cur][i]
    return graph


def dfs(cur, visited, graph,  traps, end, count):
    global min_road
    if count > min_road:
        return
    if cur == end:
        min_road = min(min_road, count)
        return
    else:
        visited[cur] = visited[cur] + 1
        if cur in traps:
            # 그래프의 모든 방향 변경
            graph = trap_change(graph, cur)
        for i in range(1, len(graph[cur])):
            if graph[cur][i] != -1:
                print(i)
                if i in traps:
                    if visited[i] < 2:
                        count += graph[cur][i]
                        dfs(i, (visited), deepcopy(graph),
                            traps, end, count)
                else:
                    if visited[i] < 1:
                        count += graph[cur][i]
                        dfs(i, (visited), deepcopy(graph),
                            traps, end, count)


print(solution(4, 1, 4,  [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
