import math


def n_to_k(n, k):
    rev_base = ""

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]


def primenumber(x):
    if x == 1:
        return False

    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
            return False
    return True


def solution(n, k):
    answer = 0
    my_n = n_to_k(n, k)

    start = 0
    end = 0
    check = ""
    for i in my_n:
        if i != '0':
            end += 1
        else:
            check = str(my_n[start:end])

            if(check != "" and primenumber(int(check))):
                answer += check_is_new_prime(start, end, my_n)
            start = end+1
            end += 1
    # 마지막이 0 으로 끝나지 않으면 체크를 못하기 때문에 여기서 체크해준다.
    check = str(my_n[start:end])
    if(check != "" and primenumber(int(check))):
        answer += check_is_new_prime(start, end, my_n)
    return answer


def check_is_new_prime(start, end, n):
    if start == 0:
        return 1
    elif end == (len(n)):
        return 1
    elif n[start-1] == '0' and n[end] == '0':
        return 1
    else:
        return 0


solution(437674, 3)
