'''
******* 문제 푼 후 느낀 것 *********
'''

'''
2022/04/16
boj.kr/10816

숫자 카드 2

문제 :

숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.
숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.


결과 :
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())

exist_card = list(map(int, input().split()))

dict1 = dict()
for k in exist_card:
    if k in dict1:
        dict1[k] += 1
    else:
        dict1[k] = 1
m = int(input())

check_list = list(map(int, input().split()))

exist_card = sorted(exist_card)

for card in check_list:
    min_idx = 0
    max_idx = n-1

    check = 0
    while(max_idx >= min_idx):
        mid_idx = (max_idx+min_idx)//2

        if(card > exist_card[mid_idx]):
            min_idx = mid_idx + 1
        elif(card < exist_card[mid_idx]):
            max_idx = mid_idx - 1
        else:
            check = 1
            break
    if(check):
        print(dict1[card], end=" ")
    else:
        print(0, end=" ")
