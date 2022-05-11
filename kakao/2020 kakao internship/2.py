def solution(expression):
    answer = 0

    calculate("*", "+", "-", expression)
    return answer


def calculate(first, second, third, expression):

    third_list = expression.split(third)
    second_list = []
    first_list = []
    for i in third_list:
        second_list += i.split(second)
    for i in second_list:
        first_list += i.split(first)

    print(third_list)
    print(second_list)
    print(first_list)

    for i in first_list:
        if i not in second_list:
            if first == "*":


solution("100-200*300-500+20")
