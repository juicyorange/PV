'''
2022/03/27
boj.kr/1676

팩토리얼 0의 개수

문제 : 
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력 :
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

결과 :
첫째 줄에 구한 0의 개수를 출력한다.

'''
import sys
input = sys.stdin.readline

num = int(input())

if num == 0:
    print(0)
else:
    result = 1
    for i in range(1, num+1):
        result = result*i

    count = 0
    for i in reversed(str(result)):
        if i == "0":
            count += 1
        else:
            break
    print(count)
