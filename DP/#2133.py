'''
# 다시해보기
2022/01/11
boj.kr/2133


타일 채우기

문제 : 

3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.

입력 : 첫째 줄에 N(1 ≤ N ≤ 30)이 주어진다.
결과 : 첫째 줄에 경우의 수를 출력한다.
'''

num = int(input())

arr = [0] * (40)

arr[1] = 0
arr[2] = 3
arr[3] = 0

if(num % 2 == 0):
    for i in range(4, num+1):
        if(i % 2 == 0):
            arr[i] += arr[i-2]*3
            for j in range(2, i-2, 2):
                arr[i] += arr[j]*2
            arr[i] += 2
print(arr[num])
