def minimumWaitingTime(queries):
    # Write your code here.
    total_waiting_time = 0
    queries.sort()
    queries_length = len(queries)

    for idx, v in enumerate(queries):
        # if last
        total_waiting_time += (v * (queries_length - (idx + 1)))

    return total_waiting_time
