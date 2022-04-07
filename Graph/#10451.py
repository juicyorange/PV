'''
# 아직까지도 시간초과가 나오면 어떻게 해결해야할지 고민하는 것이 어렵다.
꼭 다시 해보기 

2022/04/05
boj.kr/10451

순열 사이클

문제 : 페이지 참조

입력 :
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

결과 :
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

# 너무 그래프의 정형화된 것(? 공식적으로 나와있는 알고리즘?)만 이용하여 구하려다 보니 오류가 발생하는 것 같다. 
문제를 보고 좀 더 유연하게 사고하여 더 짧은 알고리즘으로 해결할 수 있도록 유도하는 것이 중요할 것 같다.

'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
count = 0


def dfs(start, visited):
    global count

    visited.append(start)

    if(test_list[start] not in visited):
        dfs(test_list[start], visited)
    else:
        count += 1
        return


'''
def bfs(graph, start, visited):
    visited.append(start)

    queue = []
    queue.append(start)

    while(queue):
        node = queue.pop(0)
        for i in range(1, len(graph)):
            if(graph[node][i] == 1):
                if (i not in visited):
                    visited.append(i)
                    queue.append(i)
                elif(i == start):
                    return 1
    return 0
'''


for i in range(int(input())):
    num = int(input())
    test_list = [0] + list(map(int, input().split()))
    visited = []

    count = 0

    for i in range(1, len(test_list)):
        if(i not in visited):
            dfs(i, visited)

    print(count)
