'''
2022/03/17
boj.kr/10820

문자열 분석

문제:
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.

입력 :
첫째 줄부터 N번째 줄까지 문자열이 주어진다. (1 ≤ N ≤ 100) 문자열의 길이는 100을 넘지 않는다.

결과 :
첫째 줄부터 N번째 줄까지 각각의 문자열에 대해서 소문자, 대문자, 숫자, 공백의 개수를 공백으로 구분해 출력한다.
'''
import sys
input = sys.stdin.readline

for i in range(100):
    input_string = input().rstrip('\n')

    if not input_string:
        break

    l, u, d, s = 0, 0, 0, 0

    for c in input_string:
        if c.islower():
            l += 1
        elif c.isupper():
            u += 1
        elif c.isspace():
            s += 1
        elif c.isdigit():
            d += 1

    print(l, u, d, s)
