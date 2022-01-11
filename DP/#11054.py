'''
# 11053과 유사한 문제
# 이 문제는 나중에 11053 을 까먹었을때 다시 풀어보면 좋을 것 같다. 지금은 이전의 문제를 풀었기 떄문에  문제 없이 풀 수 있었던 것 같다.
2022/01/05
boj.kr/11054

가장 긴 바이토닉 부분 수열

문제 : 
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.


입력 :
첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

결과 :
첫째 줄에 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력한다.


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
        if(arr[k] < arr[i]):
            dp[i] = max(dp[i], dp[k]+1)

for i in range(num):
    for k in range(i):
        if(arr[k] > arr[i]):
            dp[i] = max(dp[i], dp[k]+1)

print(max(dp))
