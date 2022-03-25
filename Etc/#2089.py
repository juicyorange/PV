'''
2022/03/25
boj.kr/2089

-2진수

문제:
-2진법은 부호 없는 2진수로 표현이 된다. 2진법에서는 20, 21, 22, 23이 표현 되지만 -2진법에서는 (-2)0 = 1, (-2)1 = -2, (-2)2 = 4, (-2)3 = -8을 표현한다. 
10진수로 1부터 표현하자면 1, 110, 111, 100, 101, 11010, 11011, 11000, 11001 등이다.
10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성하시오.

입력 :
첫 줄에 10진법으로 표현된 수 N이 주어진다.

결과 :
-2진법 수를 출력한다.
'''
import sys
input = sys.stdin.readline

num = int(input())
result = ""
while(1):
    r = num % -2
    if(r == -1):
        if(num > 0):
            num = int(num/-2)
        else:
            num = int(num/-2) + 1
        result += "1"
    else:
        num = int(num/-2)
        result += str(r)
    if(num == 1 or num == -1 or num == 0):
        if(num == 1):
            result += "1"
        break
if(num == -1):
    result += "11"

for i in range(len(result)-1, -1, -1):
    print(result[i], end="")
