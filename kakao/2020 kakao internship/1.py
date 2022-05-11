def solution(numbers, hand):
    answer = ''
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]

    lefthand = (3, 0)
    righthand = (3, 2)
    for number in numbers:
        for i in range(4):
            if number == keypad[i][0]:
                answer += 'L'
                lefthand = (i, 0)
                break
        for i in range(4):
            if number == keypad[i][2]:
                answer += 'R'
                righthand = (i, 2)
                break

        for i in range(4):
            if number == keypad[i][1]:
                dist_left = minus(lefthand, (i, 1))
                dist_right = minus(righthand, (i, 1))

                if(dist_left < dist_right):
                    answer += "L"
                    lefthand = (i, 1)
                elif(dist_left > dist_right):
                    answer += "R"
                    righthand = (i, 1)
                else:
                    if hand == 'right':
                        answer += "R"
                        righthand = (i, 1)
                    else:
                        answer += "L"
                        lefthand = (i, 1)

    return answer


def minus(t1, t2):
    a1, b1 = t1
    a2, b2 = t2
    return (abs(a1-a2) + abs(b2-b1))


print(solution([1, 3], 'left'))
