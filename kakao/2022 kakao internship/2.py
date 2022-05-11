from collections import deque


def solution(queue1, queue2):
    answer = -2
    my_deque = deque()
    my_deque2 = deque()

    # 그냥 큐 두개 합쳐서 인덱스 옮겨가면서 비교
    for i in queue1+queue2:
        my_deque.append(i)

    for i in queue2+queue1:
        my_deque2.append(i)
    const_queue1_len = len(queue1)
    const_queue2_len = len(queue2)
    min_move = -1

    for i in range(len(queue1)):
        # i 번 만큼 앞에서 뺴서 뒤에 넣어준다.
        check_deque = my_deque.copy()
        for _ in range(i):
            item = (check_deque.popleft())
            check_deque.append(item)

        queue1_len = const_queue1_len - i
        queue2_len = const_queue2_len + i
        move_queue1 = i

        if(queue1_len < 0):
            break

        if sum(list(check_deque)[0:queue1_len]) == sum(list(check_deque)[queue1_len:len(my_deque)+1]):
            if(min_move < 0):
                min_move = move_queue1
            else:
                min_move = min(min_move, move_queue1)
        for j in range(len(queue1) + len(queue2)):
            queue2_len = queue2_len - 1
            queue1_len = queue1_len + 1
            if queue2_len < 0:
                break
            if sum(list(check_deque)[0:queue1_len]) == sum(list(check_deque)[queue1_len:len(my_deque)+1]):
                if(min_move < 0):
                    min_move = move_queue1 + j + 1
                else:
                    min_move = min(min_move, move_queue1+j + 1)

    for i in range(len(queue2)):
        # i 번 만큼 앞에서 뺴서 뒤에 넣어준다.
        check_deque = my_deque2.copy()
        for _ in range(i):
            item = (check_deque.popleft())
            check_deque.append(item)

        queue1_len = const_queue1_len - i
        queue2_len = const_queue2_len + i
        move_queue1 = i

        if(queue1_len < 0):
            break

        if sum(list(check_deque)[0:queue1_len]) == sum(list(check_deque)[queue1_len:len(my_deque)+1]):
            if(min_move < 0):
                min_move = move_queue1
            else:
                min_move = min(min_move, move_queue1)
        for j in range(len(queue1) + len(queue2)):
            queue2_len = queue2_len - 1
            queue1_len = queue1_len + 1
            if queue2_len < 0:
                break
            if sum(list(check_deque)[0:queue1_len]) == sum(list(check_deque)[queue1_len:len(my_deque)+1]):
                if(min_move < 0):
                    min_move = move_queue1 + j + 1
                else:
                    min_move = min(min_move, move_queue1+j + 1)
    answer = (min_move)
    return answer
