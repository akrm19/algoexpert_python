# write a function that takes in a non-empty array of ints that are sorted in asc order and returns
# a new array of the same length with the squares of the original ints also sorted in asc
def sortedSquaredArray(array):
    # Write your code here.
    sortNeeded = False
    squared = []
    for val in array:
        squared.append(val * val)
        if val < 0:
            sortNeeded = True
    if sortNeeded:
        squared.sort()

    return squared
