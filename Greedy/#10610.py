'''
******* 문제 푼 후 느낀 것 *********
규칙을 몰랐다면 못풀었을 것이다.
우선 3의 배수인 경우 각 자리의 합이 3의 배수가 되는 경우에만 3의 배수이다.
추가적으로 30 의 배수라 했으므로 마지막 자리가 0 이면 성립된다. 
이 조건을 인터넷을 보고 알았다. 완전탐색으로 풀려 했는데, 분명 시간초과가 발생할 것이었다. 
'''

'''
2022/04/19
boj.kr/10610

30

문제 :
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 미르코는 30이란 수를 존경하기 때문에, 
그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.

입력 :
N을 입력받는다. N는 최대 105개의 숫자로 구성되어 있으며, 0으로 시작하지 않는다.

결과 :
미르코가 만들고 싶어하는 수가 존재한다면 그 수를 출력하라. 그 수가 존재하지 않는다면, -1을 출력하라.

'''
import sys
input = sys.stdin.readline

num_string = str(input())
num_arr = []
for i in range(0, len(num_string)-1):
    num_arr.append(num_string[i])

num_arr = sorted(num_arr, reverse=1)

if('0' not in num_arr):
    print(-1)
else:
    check = 0
    for i in num_arr:
        check += int(i)
    if check % 3 != 0:
        print(-1)
    else:
        for i in num_arr:
            print(i, end="")
