'''
// 추후 제공되는 sort 말고 직접 정렬을 구현해보자

2022/03/09
boj.kr/2751

수 정렬하기 2

문제:
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.


입력 :
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

결과 :
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

number_count = int(input())

arr = [0] * number_count

for i in range(number_count):
    arr[i] = int(input())

arr.sort()

for i in range(number_count):
    print(arr[i])
