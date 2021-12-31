'''
boj.kr/10992

별 찍기 - 17

입력 4
결과 
   *
  * *
 *   *
*******
'''
num = int(input())

for i in range(num, 0, -1):
    for j in range(0, 2*num - i):
        if(i > 1):
            if(j == i-1 or j == 2*num-i-1):
                print("*", end="")
            else:
                print(" ", end="")

        else:
            print("*", end="")

    print("")
