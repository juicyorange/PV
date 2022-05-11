def solution(board, skill):
    answer = 0
    for s in skill:
        skill_type, r1, c1, r2, c2, degree = s
        if(skill_type == 1):
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] = board[i][j] - degree
        else:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] = board[i][j] + degree
    for i in board:
        for j in i:
            if(j > 0):
                answer += 1
    print(board)
    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [
      [1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
