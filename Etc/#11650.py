'''

2022/03/09
boj.kr/11650

좌표 정렬하기

문제:
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.


입력 :
첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

결과 :
첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

num = int(input())

arr = [[0 for i in range(2)] for i in range(num)]

for i in range(num):
    input1, input2 = input().split()
    arr[i][0] = int(input1)
    arr[i][1] = int(input2)


arr.sort()

for i in range(num):
    print(arr[i][0], arr[i][1])
