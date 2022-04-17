'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/04/17
boj.kr/11728

배열 합치기

문제 :
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력 :
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

결과 :
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_idx = 0
b_idx = 0

result = []

while(1):
    if(a_idx >= n or b_idx >= m):
        break

    if A[a_idx] <= B[b_idx]:
        result.append(A[a_idx])
        a_idx += 1
    else:
        result.append(B[b_idx])
        b_idx += 1


if(a_idx >= n):
    for i in range(b_idx, m):
        result.append(B[i])
elif(b_idx >= m):
    for i in range(a_idx, n):
        result.append(A[i])

print(*result)
