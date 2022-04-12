
'''
문제 푼 후 느낀 것

많이 어려웠다... 탐색을 2번 쓸것이라고는 생각치도 못했다.

또한 visited. 즉, 해당 지점을 방문 했는지 아닌지를 체크하는 것이 굉장히 중요하다는 것을 느꼈다.
이것을 제대로 하지 않으면, dfs에서는 재귀가 너무 깊어지거나, bfs에서는 queue에 중복되는 값이 들어가져
메모리가 터질 수 있다는 생각이 들었다. 

해당 문제는 그래프 문제를 고민하기 아주 좋은 문제인 것 같다. 다음에 꼭 다시 풀어보자.


'''

'''
2022/04/12
boj.kr/2146

다리 만들기

문제 : ## 그림이 있는 문제이니 사이트에 가서 확인해보기

여러 섬으로 이루어진 나라가 있다. 이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다. 
하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다. 

그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다. 이 나라는 여러 섬으로 이루어져 있으며, 섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 
다음은 세 개의 섬으로 이루어진 나라의 지도이다.


위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다. 
가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.


물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나, 
위의 경우가 놓는 다리의 길이가 3으로 가장 짧다(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).
지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.

입력 :
첫 줄에는 지도의 크기 N(100이하의 자연수)가 주어진다. 그 다음 N줄에는 N개의 숫자가 빈칸을 사이에 두고 주어지며, 0은 바다, 1은 육지를 나타낸다. 항상 두 개 이상의 섬이 있는 데이터만 입력으로 주어진다.

결과 :
첫째 줄에 가장 짧은 다리의 길이를 출력한다.
'''

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

r = [-1, 1, 0, 0]
c = [0, 0, -1, 1]


def dfs(i, j, check):
    visited[i][j] = 1
    my_map[i][j] = check
    for k in range(4):
        temp_i = i + r[k]
        temp_j = j + c[k]

        if(0 <= temp_i < n and 0 <= temp_j < n):
            if(my_map[temp_i][temp_j] == 1 and visited[temp_i][temp_j] == 0):
                dfs(temp_i, temp_j, check)


def bfs(land):
    queue = deque()
    dist = [[0 for _ in range(n)] for _ in range(n)]
    # 체크할 장소 추가
    for i in range(n):
        for j in range(n):
            if my_map[i][j] == land:
                queue.append((i, j))

    # 큐가 비어있을때까지 섬을 확장해나가는 것 진행
    while(queue):
        i, j = queue.popleft()
        for k in range(4):
            temp_i = i + r[k]
            temp_j = j + c[k]
            if(0 <= temp_i < n and 0 <= temp_j < n):
                # 여기서 메모리 초과가 발생한다. 왜냐하면 dist[temp_i][temp_j] == 0 을 해주지 않으면, 양방향에서 오는
                # 것을 모두 queue에 넣게 되기 때문이다
                # 즉, 확인해야할 값이 중복해서 들어가는 일이 발생한다는 것이다.
                # 이러한 문제를 볼때 visisted 즉, 방문 했는지 안했는지를 확인하는 것이 굉장히 중요할 것 같다.
                # 모든 문제에 들어가지만 이렇게 변환해서 풀려니 헷갈린 것 같다 주의하도록 하자.
                if(dist[temp_i][temp_j] == 0):
                    if(my_map[temp_i][temp_j] == 0):
                        dist[temp_i][temp_j] = dist[i][j] + 1
                        queue.append((temp_i, temp_j))

                    elif(my_map[temp_i][temp_j] != land):
                        # bfs 로 처음 land를 발견한 곳이 최단길이임
                        return dist[i][j]


n = int(input())

my_map = [[] for _ in range(n)]
for i in range(n):
    my_map[i] = list(map(int, input().split()))

visited = [[0 for _ in range(n)] for _ in range(n)]
check = 1

for i in range(n):
    for j in range(n):
        if(visited[i][j] == 0 and my_map[i][j] == 1):
            check += 1
            dfs(i, j, check)


temp = []

for land in range(2, check+1):
    temp.append(bfs(land))

print(min(temp))
