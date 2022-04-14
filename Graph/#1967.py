
'''
******* 문제 푼 후 느낀 것 *********
# 이 문제는 바로 전 문제가 트리의 지름에 관련된 문제라 풀이를 알기 때문에 쉽게 풀었던것 같다.
트리의 지름은 -> 트리의 한 지점에서 가장 먼곳 -> 해당 지점에서 제일 먼곳
위처럼 구하는 것을 꼭 기억했으면 한다. 

다음에 다시 해서 기억이 꼭 나도록 하자.
'''

'''
2022/04/14
boj.kr/1967

트리의 지름

문제 : ** 그림이 있으니 홈페이지 가서 참조바람

트리(tree)는 사이클이 없는 무방향 그래프이다. 
트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 
트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.

이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.

트리의 노드는 1부터 n까지 번호가 매겨져 있다.

입력 :
파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 
둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 
간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 
두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 
간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 
루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

결과 :
첫째 줄에 트리의 지름을 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
t = [[] for _ in range(n+1)]

for _ in range(n-1):
    parrent, node, weight = map(int, input().split())

    t[parrent].append((node, weight))
    t[node].append((parrent, weight))


def dfs(start, check):
    for i in range(len(t[start])):
        next_node, weight = t[start][i]
        if dist[next_node] == 0 and next_node != check:
            dist[next_node] = dist[start] + weight
            dfs(next_node, check)


dist = [0 for _ in range(n+1)]
dfs(1, 1)

max_idx = dist.index(max(dist))

dist = [0 for _ in range(n+1)]
dfs(max_idx, max_idx)
print(max(dist))
