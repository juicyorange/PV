
'''
******* 문제 푼 후 느낀 것 *********

# 처음에 모든 노드를 다 돌면서 최대값을 구하는 로직을 구현했었으나, 메모리 초과가 발생했다.
# 이 문제의 접근법은 한 노드에서 최대 거리에 있는 노드를 구하고, 또 그 노드에서 최대 거리에 있는 노드가 트리의 지름이라는 것이다. 
# 이것을 이용하니 금방 해결할 수 있었다. 
'''

'''
2022/04/14
boj.kr/1167

트리의 지름

문제 :
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.

입력 :
트리가 입력으로 주어진다.
먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2 ≤ V ≤ 100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다.
정점 번호는 1부터 V까지 매겨져 있다.

먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데,
하나는 정점번호, 다른 하나는 그 정점까지의 거리이다. 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고,
정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다. 각 줄의 마지막에는 -1이 입력으로 주어진다.

주어지는 거리는 모두 10,000 이하의 자연수이다.

결과 :
첫째 줄에 트리의 지름을 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
t = [[] for _ in range(n+1)]

for i in range(n):
    input_list = list(map(int, input().split()))
    # 문제에서 정점이 순서대로 주어진다고 한 적이 없다.
    # 다만 예시 문제에서 1,2,3,4,5 순으로 줘서 그렇게 생각했던 것이ㅏㄷ.
    # 이거 때문에 1시간 정도 날린 것 같은데, 앞으로 이런 것도 잘 보자...ㅠ
    # t[i+1] = input_list
    t[input_list[0]] = input_list


def dfs(start, check, dist):
    for i in range(1, len(t[start]), 2):
        next_start = t[start][i]
        if next_start == -1:
            return
        elif(dist[next_start] == 0 and next_start != check):
            next_dist = t[start][i+1]
            dist[next_start] = dist[start] + next_dist
            dfs(next_start, check, dist)


dist1 = [0 for _ in range(n+1)]
dfs(1, 1, dist1)
dist1[1] = 0

next_find = dist1.index(max(dist1))

dist2 = [0 for _ in range(n+1)]
dfs(next_find, next_find, dist2)
dist2[next_find] = 0


print(max(dist2))

'''

def dfs(start, check):
    for i in range(1, len(t[start]), 2):
        next_start = t[start][i]
        if next_start == -1 or next_start == check:
            return
        elif(dist[check][next_start] == 0):
            next_dist = t[start][i+1]
            dist[check][next_start] = dist[check][start] + next_dist
            dfs(next_start, check)


max_value = 0
for i in range(1, n+1):
    dfs(i, i)
    max_value = max(max_value, max(dist[i]))

print(dist)
print(max_value)
'''
