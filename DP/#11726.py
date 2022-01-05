'''
## 다시해보기 

2022/01/01
boj.kr/11726

2×n 타일링

문제 : 

2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력 : 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000
결과 : 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

###
자꾸 재귀적인 방법으로 해결하려하는데, 이것은 시간초과가 많이 나온다.
DP 방식임을 명심하고 계속해서 풀도록 하자.
'''
'''
def tyling(num):
    # 타일이 1개 아래로 남았다면 횟수를 하나 더해준다.
    if num < 2:
        if num < 0:
            return 0
        else:
            return 1
    else:
        return tyling(num-2) + tyling(num-1)


print(tyling(num) % 10007)
'''
num = int(input())

arr = [0] * 10000
arr[0] = 1
arr[1] = 2
for i in range(2, num):
    arr[i] = (arr[i-1] + arr[i-2]) % 10007

print(arr[num-1])
