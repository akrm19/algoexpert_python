# given two non-empty arrays, write a function that determines if the second
# array is a subsequence of the first one

def isValidSubsequence(array, sequence):
    curArrayIdx = 0

    for curSeqVal in sequence:
        nextArrayIdx = getNextIdxOfChar(curSeqVal, array, curArrayIdx)

        if nextArrayIdx == -1:
            return False  
        curArrayIdx = nextArrayIdx + 1

    return True

def getNextIdxOfChar(targetVal, arr, curArrayIdx):
    arrayLength = len(arr)

    while curArrayIdx < arrayLength:

        curChar = arr[curArrayIdx]
        if targetVal == curChar:
            return curArrayIdx
        else:
            curArrayIdx += 1

    return -1
