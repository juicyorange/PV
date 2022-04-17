'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/04/17
boj.kr/1780

종이의 개수

문제 :
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다. 우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

    1. 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
    2. (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.

입력 :
첫째 줄에 N(1 ≤ N ≤ 37, N은 3k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.

결과 :
첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

paper = [[] for _ in range(n)]

for i in range(n):
    paper[i] = list(map(int, input().split()))

result = [0]*3


def paper_divide(x, y, scope):

    check_value = paper[x][y]
    is_not_same = 0

    if(scope == 1):
        result[check_value+1] = result[check_value+1] + 1
        return

    for i in range(scope):
        if(is_not_same):
            break
        for j in range(scope):
            if paper[x+i][y+j] != check_value:
                is_not_same = 1
                break

    if(is_not_same):
        for i in range(0, scope, scope//3):
            for j in range(0, scope, scope//3):
                paper_divide(x+i, y+j, scope//3)
    else:
        result[check_value+1] = result[check_value+1] + 1


paper_divide(0, 0, n)
for i in result:
    print(i)
