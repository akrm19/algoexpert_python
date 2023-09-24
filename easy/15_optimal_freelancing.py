def optimalFreelancing(jobs):
    # Write your code here.
    total_pay = 0
    available_days = 7
    day_availability = [True] * available_days
    jobs.sort(key=lambda job: job["payment"], reverse=True)

    for job in jobs:
        payment = job["payment"]
        deadline = job["deadline"]
        deadline = min(deadline, available_days)

        for day_idx in reversed(range(deadline)):
            if day_availability[day_idx] is True:
                day_availability[day_idx] = False
                total_pay += payment
                break

    return total_pay

def optimalFreelancing2(jobs):
    # Write your code here.
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    days_available = 7
    day_availability = [True] * days_available
    total_pay = 0

    for job in jobs:
        payment = job["payment"]
        deadline = job["deadline"]
        max_date = min(deadline, days_available)

        for day_idx in reversed(range(max_date)):
            if day_availability[day_idx] is True:
                day_availability[day_idx] = False
                total_pay += payment
                break

    return total_pay