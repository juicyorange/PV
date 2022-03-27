'''
2022/03/27
boj.kr/10872

팩토리얼

문제 : 
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력 :
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

결과 :
첫째 줄에 N!을 출력한다.

'''
import sys
input = sys.stdin.readline

num = int(input())

if num == 0:
    print(1)
else:
    result = 1
    for i in range(1, num+1):
        result = result*i
    print(result)
