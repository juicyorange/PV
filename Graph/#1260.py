'''
# 이거는 꼭 DFS, BFS 구현하는 방법을 익혀놓자... 
2022/03/27
boj.kr/1260

DFS와 BFS

문제 :
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력 :
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

결과 :
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

'''
import sys
input = sys.stdin.readline


def DFS(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited)

    return visited


def BFS(graph, start):
    visited = []
    visited.append(start)

    queue = []
    queue.append(start)

    while queue:
        node = queue.pop(0)

        for i in range(1, len(graph)+1):
            if i not in visited and i in graph[node]:
                queue.append(i)
                visited.append(i)
    return visited


n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for j in graph:
    j.sort()

dfs_result = (DFS(graph, v))
print(*dfs_result)

bfs_result = (BFS(graph, v))
print(*bfs_result)
