def binarySearch(array, target):
    # Write your code here.
    low_idx = 0
    high_idx = len(array) - 1

    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        mid_val = array[mid_idx]
        if mid_val == target:
            return mid_idx
        elif target < mid_val:
            high_idx = mid_idx - 1
        else:
            low_idx = mid_idx + 1

    return -1
