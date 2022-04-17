'''
******* 문제 푼 후 느낀 것 *********
흠.. 오늘 푼 문제중에 비슷한 유형의 문제가 있었다.  
#1780 종이 나누기 문제와 비슷한 유형이었는데, 과연 이 문제를 풀지 않고
처음부터 이 문제를 보았을때 풀 수 있었을까..? 하는 의문이 들었다. 

나중에 한번 더 풀어보면 도움이 될 것 같다.
'''

'''
2022/04/17
boj.kr/1992

쿼드 트리

문제 :
흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 
흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 
이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다

입력 :
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

결과 :
첫째 줄에 옮긴 횟수 K를 출력한다.
두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = [[] for _ in range(n)]

for i in range(n):
    input_str = str(input())
    for k in range(len(input_str)-1):
        arr[i].append(int(input_str[k]))


def divide(x, y, scope):
    check_value = arr[x][y]
    diff = 0
    for i in range(scope):
        if diff:
            break
        for j in range(scope):
            if check_value != arr[x+i][y+j]:
                diff = 1
                break

    if(diff == 0):
        print(check_value, end="")
    else:
        print("(", end="")

        for i in range(0, scope, scope//2):
            for j in range(0, scope, scope//2):
                divide(x+i, y+j, scope//2)
        print(")", end="")


divide(0, 0, n)
