'''
2022/03/25
boj.kr/1929

소수 구하기

문제:
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력 :
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

결과 :
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 1/2 에 대한 것이 소수인가 검사하는 것 보다 **0.5 인 것에 대해 소수인지 찾는게 더 빠르다.
# 또한 이 방법 말고 '에라토스테네스의 체' 라는 개념이 있는데 2부터 시작해서 배수를 지워나가면 나머지는다 소수만 남는다는 것을 알 수 있다. 
# 에라토스테네스의 체 알고리즘은 다수의 소수를 찾아야 하는 문제에서 효과적이다. 시간복잡도가 O(nln(ln n ))) 이다. 거의 선형 가까울 정도로 빠르다.
'''
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

for i in range(a, b+1):
    if(i != 1):
        result = True
        for j in range(2, int(i**0.5)+1):
            if(i % j == 0):
                result = False
                break
            else:
                result = True
        if(result):
            print(i)
