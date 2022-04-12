'''
문제 푼 후 느낀 것!

dfs 는 최단거리를 구할때 적합하지 못하다. 왜냐하면 끝까지 가봐야 그 결과를 알 수 있기 때문이다.
하지만 bfs는 멈춘 순간 최단거리이기 때문에 최단거리를 구하는데 적합하다.
단, 가중치가 0,1 인 경우에 적합하다고 느꼈다.

그렇지 않으면 dfs 나 bfs나 끝까지 갔을때 가중치가 어떤 것이 나올지 모르기 때문에 비슷하다고 생각된다.

사실 dfs도 한번 쭉 내려간 다음에 min 값을 설정해주고, 다시 재귀를 돌때 그 min 값을 넘는 것은 검사하지 않으면 되지 않나?
-> 이거 이해하면 좋을 것 같다.

결국에는 시간초과가 발생한다. bfs는 주변에 있는 것들을 바로바로 확인하면서 가기 때문에 최종 목적지에 도착하자마자
그것이 최솟값이지만, dfs는 쭉 아래로 탐색을 한 뒤 이어간다. 그 결과 재귀를 너무 많이 반복하게 되서 시간복잡도가 넘어가 오류가 발생하게 된다.

# 다음에 다시 해보기
'''

'''
2022/04/12
boj.kr/2718

미로 탐색

문제 : ## 그림이 있는 문제이니 사이트에 가서 확인해보기

N×M크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.

한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력 :
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

결과 :
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

c = [-1, 1, 0, 0]
r = [0, 0, -1, 1]

n, m = map(int, input().split())

graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    string_input = str(input())
    for j in range(m):
        graph[i][j] = int(string_input[j])


queue = []
queue.append((0, 0))
'''
# Dfs 를 하는데, min 값을 두고, min 값보다 크면 더 이상 탐색을 하지 않는 방식으로 구현?
# 이 방법으로 하면 너무 경우가 많아 진다.
# 결국에는 무조건 일단 끝까지 가면 멈추긴 하는데, 그 이후 다른 경로를 어떻게 찾아서 나가야 할지 모르겠다.


def dfs(i, j):
    for k in range(4):
        temp_i = i + c[k]
        temp_j = j + r[k]

        if (0 <= temp_i < n and 0 <= temp_j < m):
            if(graph[temp_i][temp_j] == 1):
                if(visited[temp_i][temp_j] == 0 or visited[temp_i][temp_j] > visited[i][j] + 1):
                    visited[temp_i][temp_j] = visited[i][j] + 1
                    if(temp_i == n-1 and temp_j == m-1):
                        return
                    dfs(temp_i, temp_j)


visited[0][0] = 1
dfs(0, 0)
print(visited[n-1][m-1])

'''


def bfs():
    while(queue):
        i, j = queue.pop(0)
        for k in range(4):
            temp_i = i + c[k]
            temp_j = j + r[k]

            if(0 <= temp_i < n and 0 <= temp_j < m):
                if(graph[temp_i][temp_j] == 1):
                    queue.append((temp_i, temp_j))
                    graph[temp_i][temp_j] = graph[i][j] + 1


bfs()
print(graph[n-1][m-1])
