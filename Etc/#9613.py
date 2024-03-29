'''
2022/03/22
boj.kr/9613

gcd 합

문제:
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 
각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

결과 :
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
'''
import sys
input = sys.stdin.readline


def gcd(a, b):
    while (b > 0):
        temp = a % b
        a = b
        b = temp
    return a


num = int(input())

for i in range(num):
    arr = list(map(int, input().split()))
    result = 0

    for j in range(1, len(arr)):
        for k in range(j+1, len(arr)):
            result += (gcd(arr[j], arr[k]))

    print(result)
