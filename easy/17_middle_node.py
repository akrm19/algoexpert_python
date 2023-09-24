# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    mid = linkedList
    fast = linkedList

    while fast.next is not None:
        fast = fast.next.next
        mid = mid.next

    return mid
    mid = linkedList
    fast = linkedList

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        mid = mid.next

    return mid

def middleNode2(linkedList):
    # Write your code here.
    length = 0
    cur = linkedList
    while cur is not None:
        length += 1
        cur = cur.next

    cur = linkedList
    middle_pos = (length // 2) + 1
    for _ in range(middle_pos):
        cur = cur.next

    return cur

def middleNode3(linkedList):
    # Write your code here.
    length = 0
    cur = linkedList
    while cur is not None:
        length += 1
        cur = cur.next

    middle_pos = (length // 2) + 1

    length = 1
    cur = linkedList
    while length < middle_pos:
        length += 1
        cur = cur.next

    return cur
