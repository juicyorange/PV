'''
2022/03/22
boj.kr/11005

진법 변환 2

문제:
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력 :
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

결과 :
첫째 줄에 10진법 수 N을 B진법으로 출력한다.
'''
import sys
input = sys.stdin.readline

N, B = map(int, input().split())

result = []

while(N >= B):
    q = int(N / B)
    r = N % B

    result.append(r)
    N = q

result.append(N)
result = reversed(result)

for i in result:
    if(i < 10):
        print(i, end="")
    else:
        print(chr(ord('A')+i - 10), end="")
