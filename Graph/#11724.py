'''
2022/03/28
boj.kr/11724

DFS와 BFS

문제 :
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
(1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

결과 :
첫째 줄에 연결 요소의 개수를 출력한다.

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


# 이거로 풀게되면 최대 재귀 깊이를 초과하여 오류가 난다.
# 해결하려면 sys.setrecursionlimit(1000000) 을 해주면 에러 없이 실행된다.
def DFS(graph, start, visited):
    visited.append(start)
    for j in range(1, len(graph)):
        if graph[start][j] == 1 and j not in visited:
            DFS(graph, j, visited)
    return visited


def BFS(graph, start):
    visisted = []
    visisted.append(start)

    queue = []
    queue.append(start)

    while(queue):
        node = queue.pop(0)

        for i in range(1, len(graph)):
            if graph[node][i] == 1 and i not in visisted:
                queue.append(i)
                visisted.append(i)
    return visisted


graph = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

v = []
count = 0
while (len(v) < len(graph)-1):
    for i in range(1, len(graph)):
        if i not in v:
            dfs = BFS(graph, i)
            count += 1
            for j in dfs:
                v.append(j)

print(count)
