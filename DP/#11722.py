'''

2022/01/05
boj.kr/11053

가장 긴 감소하는 부분 수열

문제 : 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.


입력 :
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

결과 :
첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

# 11053과 유사한 문제
'''

num = int(input())

arr = [0] * num

if (num < 1 or num > 1000):
    print("range error")
else:
    temp = list(map(int, input().split()))
    for k in range(num):
        arr[k] = temp[k]

dp = [1] * num

for i in range(num):
    for k in range(i):
        if(arr[k] > arr[i]):
            dp[i] = max(dp[i], dp[k]+1)


print(max(dp))
