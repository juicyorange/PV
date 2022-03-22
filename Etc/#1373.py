'''
2022/03/22
boj.kr/1373

2진수 8진수

문제:
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

입력 :
첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

결과 :
첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.
'''
import sys
input = sys.stdin.readline

input_string = str(input())

binary = '0b' + input_string
ten = int(binary, 2)
oct_string = oct(ten)
for i in range(2, len(oct_string)):
    print(oct_string[i], end="")


# print(format((int(input(), 2)), 'o'))
