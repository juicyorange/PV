'''
boj.kr/10991

별 찍기 - 16

입력 4
결과 
   *
  * *
 * * *
* * * *
'''
num = int(input())

for i in range(num, 0, -1):
    for j in range(0, 2*num - i):
        if(i-1 > j):
            print(" ", end="")
        else:
            if(i % 2 == 0):
                if(j % 2 == 0):
                    print(" ", end="")
                else:
                    print("*", end="")
            else:
                if(j % 2 == 0):
                    print("*", end="")
                else:
                    print(" ", end="")
    print("")
