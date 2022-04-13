
'''
******* 문제 푼 후 느낀 것 *********
생각없이 풀다가 시간초과가 발생했다...
n의 수가 엄청 큰 경우 반복문을 쓸때 고려해서 코드를 구성할 필요가 있는 것 같다.

여기서는 break 없이 모든 노드들을 계속 방문하는 방법을 사용하고 있다. (dfs 안에 print를 해보면 12개가 주어진 경우 24번, 7개는 14번을 돌고 있다.)
visited 를 사용해서 방문을 체크하면, 끝까지 갈 수 없고, 
그렇다고 visited를 사용해서 특정 노드만 찾고 나오는 코드를 구현해보았더니(아래에 있다) 시간초과가 나왔다.

시간초과는 정말 어려운 것 같다. 
'''

'''
2022/04/13
boj.kr/11725

트리의 부모 찾기

문제 : 

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

결과 :
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, (input().split()))
    arr[a].append(b)
    arr[b].append(a)

'''
#기존 방식으로 하게되면 1000000개를 찾기 위해서는 10000000 번을 반복해야한다.
#따라서 시간 초과가 발생할 수 밖에 없다. 
def dfs(start, find):
    if(visited[start] == 1):
        return
    visited[start] = 1

    for next in arr[start]:
        if next == find:
            print(start)
            return
        elif visited[next] != 1:
            dfs(next, find)


for i in range(2, n+1):
    visited = [0 for _ in range(n+1)]
    dfs(1, i)
'''
# 어차피 1부터 시작해서 방문하지 않은 노드가 없을때 까지 할 것이니 visited에 해당 노드들의 부모를 적는 방식으로 구현하자.


def dfs(start):
    '''
    이 부분을 제거하는 이유가 그냥 방문 했어도 다시 돌아서 다른 트리에 있는 곳으로 갈 수 있기 때문이다.
    어차피 노드의 개수가 1000000 개 이어도 결국 2000000 번만 하면 되기 때문에 이것이 훨씬 효율적이다.
    if(visited[start] != 0):
        return
    '''
    for next in arr[start]:
        if visited[next] == 0:
            visited[next] = start
            dfs(next)


visited = [0 for _ in range(n+1)]
dfs(1)

for i in range(2, n+1):
    print(visited[i])
