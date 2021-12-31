'''
boj.kr/11022

A + B - 9

입력 :
5
1 1
2 3
3 4
9 8
5 2

결과 :
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
'''
num = int(input())

i = 1
while(i <= num):
    a, b = input().split()

    if(0 < int(a) and int(b) < 10):
        print("Case #{0}: {1} + {2} = {3}".format(i,
                                                  int(a), int(b), int(a)+int(b)))
        i += 1
