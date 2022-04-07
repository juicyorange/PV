'''
2022/04/07
boj.kr/9466

텀 프로젝트

문제 :
이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다.
심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다. 프로젝트 팀을 구성하기 위해,
모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.) 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나, s1이 s2를 선택하고,
s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.

    1	2	3	4	5	6	7
    3	1	3	7	3	4	6

위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.

주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.

입력 :
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어진다.
각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어진다. (모든 학생들은 1부터 n까지 번호가 부여된다.)

결과 :
각 테스트 케이스마다 한 줄에 출력하고, 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 된다.


아니 이거 왜 틀렸다고 하는지 모르겠따... 
아래부분에 내가 맞다고 생각하는 코드를 올려두었다.

'''

import sys
'''
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())

result = []


def dfs(check):
    global result
    visited[check] = 1
    team.append(check)
    w = students[check]

    if(visited[w] == 1):
        if w in team:
            result += team[team.index(w):]
        return
    else:
        dfs(w)


for _ in range(n):
    how_many_people = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [0] * (how_many_people + 1)
    result = []

    for i in range(1, len(students)):
        if(visited[i] == 0):
            team = []
            dfs(i)
    print(how_many_people - len(result))


'''
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

n = int(input())

result = 0


def dfs(check, start, count):

    global result
    visited[check] = 1
    w = students[check]

    if(visited[w] == 1):
        if (start == w):
            result += count+1
        elif(check == w):
            result += 1
        return count
    else:
        count += 1
        dfs(w, start, count)


for _ in range(n):
    how_many_people = int(input())
    students = [0] + list(map(int, input().split()))

    visited = [0] * (how_many_people + 1)
    result = 0

    for i in range(1, len(students)):
        if(visited[i] == 0):
            count = 0
            dfs(i, i, count)
    print(how_many_people - result)
