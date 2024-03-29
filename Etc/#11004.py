'''

2022/03/15
boj.kr/11004

K 번째 수

문제:
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.


입력 :
첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

결과 :
A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.
'''
import sys

number_count, front = map(int, sys.stdin.readline().split())

number_list = list(map(int, sys.stdin.readline().split()))

number_list.sort()

print(number_list[(front)-1])
