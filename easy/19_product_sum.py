# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    return getSpecialArraySum(array, 1)

def getSpecialArraySum(array, depth):
    total = 0
    for item in array:
        if type(item) is list:
            total += getSpecialArraySum(item, depth + 1)
        else:
            total += item
    return total * depth