from copy import deepcopy


def solution(rc, operations):
    answer = [[]]
    my_rc = deepcopy(rc)
    for cmd in operations:
        if cmd == "ShiftRow":
            for i in range(1, len(rc)):
                rc[i] = my_rc[i-1]
            rc[0] = my_rc[len(my_rc)-1]
            my_rc = deepcopy(rc)
        if cmd == "Rotate":
            temp = deepcopy(my_rc[1][0])
            for i in range(len(my_rc)):
                for j in range(len(my_rc)):
                    if i == 0 and j < len(my_rc[0])-1:
                        rc[i][j+1] = my_rc[i][j]
                    elif i == len(my_rc)-1 and 0 < j:
                        rc[i][j-1] = my_rc[i][j]
                    elif j == len(my_rc[0])-1 and i < len(my_rc)-1:
                        rc[i+1][j] = my_rc[i][j]

                    elif j == 0 and 0 < i:
                        rc[i-1][j] = my_rc[i][j]

            rc[0][0] = deepcopy(temp)
            my_rc = deepcopy(rc)

    answer = deepcopy(rc)
    return answer
