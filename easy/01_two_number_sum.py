# Write a function that takes in a non-empty array of distinct ints and an int
# representing a target sum. If any of the 2 numbers in the input sum up to the 
# target, the func should return them in an array otherwise it should return an empty array

from operator import le


def twoNumberSum(array, targetSum):
    # Write your code here.
    if (len(array) < 2):
        return []

    existingNums = {}

    for index, val in enumerate(array):
        neededNum = targetSum - val
        print(f"target is {targetSum}, current num is {val}. Needed num is: {neededNum}")
        
        if(neededNum in existingNums.keys()):
            return [val, neededNum]
        else:
            existingNums[val] = index

    return []


def twoNumberSum2(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        curSum = array[left] + array[right]
        if curSum == targetSum:
            return [array[left], array[right]]
        elif curSum < targetSum:
            left += 1
        else:
            right -= 1
            
    return []
        



