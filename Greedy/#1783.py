'''
******* 문제 푼 후 느낀 것 *********
경우의 수를 그냥 모두 생각해보면서 적다보니
if 문이 매우 많아졌다. 

나중에는 그 규칙을 좀 생각하면서 코드 길이를 줄일 수 있도록 해야겠다. 
'''

'''
2022/04/19
boj.kr/1783

병든 나이트

문제 :
병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다. 병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.

    2칸 위로, 1칸 오른쪽
    1칸 위로, 2칸 오른쪽
    1칸 아래로, 2칸 오른쪽
    2칸 아래로, 1칸 오른쪽

병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다. 
병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다. 이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.

체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.

입력 :
첫째 줄에 체스판의 세로 길이 N와 가로 길이 M이 주어진다. N과 M은 2,000,000,000보다 작거나 같은 자연수이다.

결과 :
병든 나이트가 여행에서 방문할 수 있는 칸의 개수중 최댓값을 출력한다.

'''
import sys
input = sys.stdin.readline

n, m, = map(int, input().split())


visit_count = 1

if n == 1:
    print(visit_count)

elif(n == 2):
    if m >= 7:
        print(4)
    elif m >= 5:
        print(3)
    elif m >= 3:
        print(2)
    else:
        print(1)

else:
    if m == 1:
        print(visit_count)
    elif(m == 2):
        visit_count += 1
        print(visit_count)
    elif(m == 3):
        visit_count += 2
        print(visit_count)
    elif(m == 4):
        visit_count += 3
        print(visit_count)
    elif(m == 5):
        visit_count += 3
        print(visit_count)
    elif(m == 6):
        visit_count += 3
        print(visit_count)
    elif(m == 7):
        visit_count += 4
        print(visit_count)
    else:
        visit_count += 4
        spare_m = m - 7
        visit_count += spare_m
        print(visit_count)
