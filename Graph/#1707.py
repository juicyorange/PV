'''
2022/03/28
boj.kr/1707

이분 그래프

문제 :
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

입력 :
입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다. 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

결과 :
K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

##################################################################################################
처음에는 [1][1] = 1 이런식으로 그래프를 구현했더니 메모리초과라는 에러가 나서
[1] = [1, 2, 3] 이런식으로 해당 노드가 가진 연결점을 배열에 넣어주는 형식으로 변경하였다.

하지만 변경을 하니 이번에는 시간초과라는 오류가 나오게 되었다. 왜 그럴까 생각해보았다. 
그 이유는 pop(0) 을 하였기 때문이다. 그냥 단순히 pop() 을 하게되면 제일 뒤에있는 item 을 꺼내오는 것이기 때문에
시간 복잡도가 O(1) 이다. 하지만, pop(0) 의 경우에는 다르다. 제일 앞에있는 item 을 꺼내고 모든 항목을 한칸씩 앞으로 땡켜주는 작업을 수행해야한다.

이 떄문에 시간초과라는 오류가 출력된 것 같다. 

생각해본 방식으로는 2가지가 있다. 
1. 그냥 단순하게 deque 를 import 해서 사용한다.
2. pop(0) 대신에 index를 늘려서 해당 인덱스를 가져오는 방식으로 진행한다.

방법1 은 그냥 import 해서 list 대신 덱(deque)를 사용하면 되는것이기 때문에 방법2로 구현을 해보겠다. 

방법 2 대로도 해보았는데, 그래도 시간초과 오류가 발생한다...
방법 1도 해보았지만 마찬가지이다.

찾아보니 visited 를 bfs 를 수행할떄마다 새로 생성해서 문제가 생기는 것 같았다. 
그래서 bfs 안에서 visited 를 초기화주던 것을 밖으로 내보내고, visited에 들어있지 않은 항목은 검사를 수행하지 않도록 하였다.
(이전에는 bfs 안에서 생성된 visited 를 넘겨서, 방문한 것들을 저장하고, 방문한 노드에 대해서는 bfs 를 수행하지 않도록 했었다.)

그 결과 정상적으로 돌아갔다. 

시간초과나 메모리와 관련된 문제에서는 어떤 함수를 수행할때 그 안에서 필요한 것들을 생성하는데 시간이 오래걸리지는 않는지 꼭 확인해볼 필요가 있을 것 같다.. ㅠ

'''
import sys
input = sys.stdin.readline


def bfs(graph, start):
    now = 1
    visited[start] = now

    queue = []
    queue.append(start)
    idx = 0
    while (idx < len(queue)):
        node = queue[idx]
        now = now * (-1)
        for i in graph[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[node]*(-1)
            else:
                if(visited[i] == visited[node]):
                    print("NO")
                    return False
        idx += 1
    return True


num = int(input())

for i in range(num):
    n, m = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [0 for _ in range(len(graph))]
    for i in range(1, len(graph)):
        if visited[i] == 0:
            result = bfs(graph, i)
            if(result == False):
                break
    if result:
        print("YES")
