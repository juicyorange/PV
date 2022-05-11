import math


def solution(fees, records):
    answer = []
    base_time = fees[0]
    base_fee = fees[1]
    per_time = fees[2]
    per_fee = fees[3]

    in_out_dict = dict()
    for record in records:
        time, number, state = record.split(" ")
        if number not in in_out_dict:
            in_out_dict[number] = [time]
        else:
            in_out_dict[number].append(time)
    order_number = sorted(in_out_dict.keys())
    print(order_number)
    for record in order_number:
        time = 0
        if len(in_out_dict[record]) % 2 == 0:
            for i in range(0, len(in_out_dict[record]), 2):
                time1h, time1m = in_out_dict[record][i].split(":")
                time2h, time2m = in_out_dict[record][i+1].split(":")
                time += (int(time2h)*60 + int(time2m)) - \
                    (int(time1h)*60 + int(time1m))
        else:
            for i in range(0, len(in_out_dict[record])-1, 2):
                time1h, time1m = in_out_dict[record][i].split(":")
                time2h, time2m = in_out_dict[record][i+1].split(":")
                time += (int(time2h)*60 + int(time2m)) - \
                    (int(time1h)*60 + int(time1m))
            time1h, time1m = in_out_dict[record][-1].split(":")
            time += (23*60 + 59) - (int(time1h)*60 + int(time1m))

        if(time <= base_time):
            answer.append(base_fee)
        else:
            answer.append(
                base_fee + (math.ceil((time-base_time) / per_time)) * per_fee)
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
                                      "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
