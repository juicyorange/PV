def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    report_log = [[""] for _ in range(len(id_list))]
    for i in range(len(id_list)):
        report_log[i][0] = id_list[i]

    for c in set(report):
        reporter, reported = c.split(" ")
        for i in range(len(id_list)):
            if report_log[i][0] == reported:
                report_log[i].append(reporter)
                break

    for i in range(len(id_list)):
        temp_result = []
        for value in report_log[i]:
            if value not in temp_result:
                temp_result.append(value)
        report_log[i] = temp_result

    print(report_log)
    for i in range(len(id_list)):
        if(len(report_log[i]) > k):
            for j in range(1, len(report_log[i])):
                answer[id_list.index(report_log[i][j])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
print(solution(id_list, report, k))
