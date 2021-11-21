from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, obj):
        return isinstance(obj, ListNode) and obj is not None and obj.val == self.val and self.next == obj.next

    def __str__(self):
        n = self.next
        s = str(self.val)
        while n is not None:
            s += ", " + str(n.val)
            n = n.next
        return s

def test_function(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    f = True # indicate whether a non-null items exists
    head = ListNode(val=-1) # set the head of the list
    res = head # res is the "accumulator"
    carriage = 0 # carraige (if any)
    while f: # while at least an item is non empty
        n1 = l1.val if l1 is not None else 0 # get the item from the first list
        n2 = l2.val if l2 is not None else 0 # get the item from the second list
        s = n1 + n2 + carriage # sum the values with the previous carriage value
        digit = s % 10 # get the current digit
        carriage = 1 if s >= 10 else 0 # get the current carriage
        cur_node = ListNode(val=digit) # define a new node in the list
        res.next = cur_node # link the accumulator to the current node
        res = cur_node # update the accumulator
        l1 = l1 if l1 is None else l1.next # get the next item
        l2 = l2 if l2 is None else l2.next # get the next item
        f = l1 is not None or l2 is not None # set the flag
    if carriage > 0: # if the flag is still 1
        res.next = ListNode(val=carriage) # add a new digit
    return head.next