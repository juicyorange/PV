'''

2022/02/28
boj.kr/2225

합분해

문제 :
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우). 또한 한 개의 수를 여러 번 쓸 수도 있다.


입력 :
첫째 줄에 두 정수 N(1 ≤ N ≤ 200), K(1 ≤ K ≤ 200)가 주어진다.

결과 :
첫째 줄에 답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

temp_n, temp_k = (input()).split()

n = int(temp_n)
k = int(temp_k)

arr = [[0 for i in range(k+1)] for j in range(n+1)]


for i in range(1, k+1):
    arr[1][i] = i
for i in range(1, n+1):
    arr[i][1] = 1

for i in range(2, n+1):
    for j in range(2, k+1):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

print(arr[n][k] % 1000000000)
