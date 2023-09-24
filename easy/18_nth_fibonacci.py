def getNthFib(n):
    # Write your code here.
    if n is 1:
        return 0
    
    prev_two = [0, 1]
    counter = 3
    while counter <= n:
        next_fib = prev_two[0] + prev_two[1]
        prev_two[0] = prev_two[1]
        prev_two[1] = next_fib
        counter += 1
    return prev_two[1]

def getNthFib2(n):
    # Write your code here.
    n2 = 0
    n1 = 1
    cur = 1

    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    for num in range(2, n):
        cur = n1 + n2
        n2 = n1
        n1 = cur

    return cur

def getNthFib3(n):
    # Write your code here.
    memo = {1: 0, 2: 1}
    return getNthFibHelper(n, memo)

def getNthFibHelper(num, memoization):
    if num in memoization:
        return memoization[num]
    memoization[num] = getNthFibHelper(num - 1, memoization) + getNthFibHelper(num - 2, memoization)
    return memoization[num]
