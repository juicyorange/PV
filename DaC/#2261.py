
'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/04/17
boj.kr/2261

가장 가까운 두 점

문제 :
2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 자연수 n(2 ≤ n ≤ 100,000)이 주어진다. 다음 n개의 줄에는 차례로 각 점의 x, y좌표가 주어진다. 
각각의 좌표는 절댓값이 10,000을 넘지 않는 정수이다. 여러 점이 같은 좌표를 가질 수도 있다.

결과 :
첫째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.
'''

import sys
input = sys.stdin.readline
