from collections import deque


def solution(queue1, queue2):
    answer = -2
    if(len(queue1) != len(queue2) or len(queue1) > 300000 or len(queue1) < 1):
        return -1

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    if (queue1_sum + queue2_sum) % 2 != 0:
        return -1

    queue1_d = deque(queue1)
    queue2_d = deque(queue2)

    length = len(queue1) + len(queue2)

    cnt = 0
    flag = 0
    find = False

    while(flag <= length):
        flag += 1
        if(queue1_sum == queue2_sum):
            find = True
            break
        if queue1_sum < queue2_sum:
            item = queue2_d.popleft()
            queue1_d.append(item)
            queue1_sum += item
            queue2_sum -= item
            cnt += 1
        elif (queue1_sum > queue2_sum):
            item = queue1_d.popleft()
            queue2_d.append(item)
            queue2_sum += item
            queue1_sum -= item
            cnt += 1
    if (find):
        answer = cnt
    else:
        answer = -1
    return answer


solution([1, 2, 3], [4, 5, 6])
