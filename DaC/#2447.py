'''
******* 문제 푼 후 느낀 것 *********
이 문제도 마찬가지이다.
이전까지 계속 재귀적으로 푸는 문제들을 해결헀고, 이 문제 또한 재귀로 풀어야 한다는 것을 인지하고 있었다.
만약에 몰랐다면 풀 수 있었을까?
라는 의문이 든다. 꼭 다시해보자
'''

'''
2022/04/17
boj.kr/2447

별 찍기 - 10

문제 :
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***

N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력 :
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

결과 :
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]


def create_star(x, y, stars):
    if stars == 3:
        for i in range(3):
            for j in range(3):
                if(i != 1 or j != 1):
                    arr[x+i][y+j] = 1
    else:
        for i in range(0, stars, stars//3):
            for j in range(0, stars, stars//3):
                if(i != stars//3 or j != stars//3):
                    create_star(x+i, y+j, stars//3)


create_star(0, 0, n)

for i in arr:
    for j in i:
        if(j == 1):
            print("*", end="")
        else:
            print(" ", end="")
    print("")
