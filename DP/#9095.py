'''

2022/01/01
boj.kr/9095

1, 2, 3 더하기

문제 : 

정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.


입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
결과 : 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

'''

count = int(input())

for i in range(0, count):
    num = int(input())
    arr = [0] * 1000
    arr[0] = 1
    arr[1] = 2
    arr[2] = 4
    if num <= 11 and num > 0:
        for i in range(3, num):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]

        print(arr[num-1])
