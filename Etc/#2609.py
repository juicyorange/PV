'''
# 까먹고 있었던 것. 나중에도 기억이 안날 수 있으니 꼭 다시 해보기
2022/03/21
boj.kr/2609

나머지

문제 :
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

입력 :
첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

결과 :
첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

이거 까먹고있었다... 
'''
import sys
input = sys.stdin.readline


def gcd(a, b):
    while(b > 0):
        temp = a % b
        a = b
        b = temp
    return a


a, b = map(int, input().split())

a_b_gcd = gcd(a, b)
print(a_b_gcd)
print(int((a * b) / a_b_gcd))
