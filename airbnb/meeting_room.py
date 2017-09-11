def find_free_time(schedules):
    schedules = [item for person in schedules for item in person]
    schedules.sort(key=lambda x: x[0])
    intervals = [schedules[0]]
    index = 0
    for interval in schedules[1:]:
        if interval[0] <= intervals[index][1]:
            intervals[index][1] = max(interval[1], intervals[index][1])
        else:
            intervals.append(interval)
            index += 1
    available_intervals = []
    for i in range(1, index + 1):
        available_intervals.append([intervals[i - 1][1], intervals[i][0]])
    return available_intervals


print(find_free_time([[[1, 3], [6, 7]],
                      [[2, 4]],
                      [[2, 3], [9, 12]]]))

print(find_free_time([[[1, 3]]]))
