'''
# 다시하기
2022/03/09
boj.kr/11652

카드

문제:
준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.


입력 :
첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

결과 :
첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

# 딕셔너리에 lambda를 이용하여 정렬하는 방법에 대해 숙지하지!!
'''


num = int(input())


num_dict = {}

for i in range(num):
    input_value = int(input())
    if input_value in num_dict:
        num_dict[input_value] += 1
    else:
        num_dict[input_value] = 1

result = sorted(num_dict.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
