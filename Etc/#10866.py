'''
2022/03/17
boj.kr/10866
디큐 구현!
'''
import sys

input = sys.stdin.readline
command_count = int(input())
queue = list()

for i in range(command_count):
    command = list(map(str, input().split()))
    if(command[0] == 'push_back'):
        queue.append(int(command[1]))
    elif(command[0] == 'push_front'):
        queue.insert(0, int(command[1]))
    elif(command[0] == 'pop_front'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue.pop(0))
    elif(command[0] == 'pop_back'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue.pop())
    elif(command[0] == 'size'):
        print(len(queue))
    elif(command[0] == 'empty'):
        if(len(queue) != 0):
            print(0)
        else:
            print(1)
    elif(command[0] == 'back'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[len(queue)-1])
    elif(command[0] == 'front'):
        if(len(queue) == 0):
            print(-1)
        else:
            print(queue[0])
