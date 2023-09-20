def nonConstructibleChange(coins):
    # Write your code here.
    #if len(coins) == 0:
    #    return 1

    coins.sort()
    min_change_created = 0

    #for idx, coin in enumerate(coins):
    for coin in coins:
        if coin > (min_change_created + 1):
            return min_change_created + 1
        min_change_created += coin

    return min_change_created + 1
