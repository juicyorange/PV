def solution(survey, choices):
    answer = ''
    type_dict = {"R": 0, "T": 0, "C": 0,
                 "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    # 설문 반영
    for i in range(len(choices)):
        survey_type1 = survey[i][0]
        survey_type2 = survey[i][1]

        if choices[i] == 1:
            type_dict[survey_type1] += 3
        elif choices[i] == 2:
            type_dict[survey_type1] += 2

        elif choices[i] == 3:
            type_dict[survey_type1] += 1
        elif choices[i] == 4:
            # 점수 없음
            continue
        elif choices[i] == 5:
            type_dict[survey_type2] += 1
        elif choices[i] == 6:
            type_dict[survey_type2] += 2
        elif choices[i] == 7:
            type_dict[survey_type2] += 3

    # 설문 결과 찾기
    if type_dict["R"] >= type_dict["T"]:
        answer += "R"
    else:
        answer += "T"

    if type_dict["C"] >= type_dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if type_dict["J"] >= type_dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if type_dict["A"] >= type_dict["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer
