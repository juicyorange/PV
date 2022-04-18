'''
******* 문제 푼 후 느낀 것 *********
# 그냥 버블소트로 했더니 틀렸었다..
# inversion counting 이라는 방법으로 풀어야만 했다.
# 합병정렬을 하면서, 정렬할때 오른쪽에 있는 것이 왼쪽에 있는 것보다 먼저 들어가게 되면 
# 순서가 inverse 되어 있는 것으로 그 수를 count 하는 문제였다..
# 이러한 방법을 몰랐다면 전혀 풀 수 없었을 것 같다. 
inversion counting!! 

## 나중에 꼭 다시해보기

'''

'''
2022/04/18
boj.kr/1517

버블소트

문제 :
N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.

버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다. 
예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다. 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 
다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.

입력 :
첫째 줄에 N(1 ≤ N ≤ 500,000)이 주어진다. 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다. 각각의 A[i]는 0 ≤ |A[i]| ≤ 1,000,000,000의 범위에 들어있다.

결과 :
첫째 줄에 Swap 횟수를 출력한다
'''

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

sorted_list = []
count = 0


def merge_sort(start, end):
    global sorted_list
    global count
    if(start < end):
        mid = (start+end)//2
        merge_sort(start, mid)
        merge_sort(mid+1, end)

        left_start = start
        right_start = mid+1
        temp = []
        # 병합하는 부분
        while(1):
            if(left_start > mid or right_start > end):
                break
            if(arr[left_start] <= arr[right_start]):
                temp.append(arr[left_start])
                left_start += 1
            else:
                temp.append(arr[right_start])
                right_start += 1
                count = count + (mid-left_start+1)

        if (left_start <= mid):
            temp = temp + arr[left_start:mid+1]
        if (right_start <= end):
            temp = temp + arr[right_start:end+1]

        for i in range(len(temp)):
            arr[start+i] = temp[i]


merge_sort(0, n-1)
print(count)
