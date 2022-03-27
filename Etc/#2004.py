'''
# 나중에 다시 해보기!
2022/03/27
boj.kr/2004

조합 0의 개수

문제 : 
C(n,m) 의 끝자리 0 의 개수를 출력하는 프로그램을 작성하시오

입력 :
정수 n, m 이 첫째줄에 들어온다.

결과 :
첫째 줄에 C(n,m) 의 끝자리 0의 개수를 출력한다.

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 5 개수 세는 함수


def five_count(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt

# 2 개수 세는 함수


def two_count(n):
    cnt = 0
    while n != 0:
        n = n // 2
        cnt += n
    return cnt


if m == 0:
    print(0)
else:
    print(min(two_count(n)-two_count(m)-two_count(n-m),
              five_count(n)-five_count(m)-five_count(n-m)))
