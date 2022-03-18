'''
2022/03/17
boj.kr/10808

나이순 정렬

문제:
알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오

입력 :
첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

결과 :
단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.
'''
import sys
input = sys.stdin.readline

input_string = input()

alpa_dict = dict()

alpa_string = "abcdefghijklmnopqrstuvwxyz"

for i in range(len(alpa_string)):
    alpa_dict[alpa_string[i]] = 0

for i in range(len(input_string)-1):
    alpa_dict[input_string[i]] += 1

result = list(alpa_dict.values())
for i in range(len(result)):
    if(i == len(result)-1):
        print(result[i])
    else:
        print(result[i], end=" ")

'''
// 진짜 쉬운방법... 하지만 시험장에서 아스키를 외워가기는 좀 힘들거같다!
// ord 함수는 해당 문자의 유니코드 정수값을 반환한다.
arr=input()
cnt=[0]*26 
for i in arr: 
    cnt[ord(i)-ord('a')]+=1 
print(*cnt)

출처: https://youjin86.tistory.com/39 [_]
'''
