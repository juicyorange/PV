'''
2022/03/10
boj.kr/10989

수 정렬하기 3

문제:
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.


입력 :
째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

결과 :
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다

#####
메모리와 시간에 대해 고민해보게 되었다.
주어진 메모리나 시간이 작다면 최대한 메모리와 시간을 줄일 수 있는 방법을 고안해보자.
'''
import sys
number_count = int(sys.stdin.readline())

arr = [0] * 10001

for i in range(number_count):
    input_num = int(sys.stdin.readline())
    arr[input_num] += 1


for i in range(10001):
    if(arr[i] != 0):
        for j in range(arr[i]):
            print(i)
