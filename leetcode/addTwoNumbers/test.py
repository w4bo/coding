import unittest
import os
from importlib import import_module
import sys
sys.path.insert(0, 'addTwoNumbers')
from addTwoNumbers1 import ListNode
from addTwoNumbers1 import test_function

def l2ln(l):
    head = ListNode(val=-1)
    res = head
    for i in range(len(l)):
        cur_node = ListNode(val=l[i])
        res.next = cur_node
        res = cur_node
    return head.next

def ln2l(ln):
    l = []
    while ln is not None:
        l.append(ln.val)
        ln = ln.next
    return l

def unit_test(self, test_function):
    self.assertEqual(ln2l(test_function(l2ln([2, 4, 3]), l2ln([5, 6, 4]))), [7, 0, 8])
    self.assertEqual(ln2l(test_function(l2ln([2, 4, 3]), l2ln([5, 6, 4]))), [7, 0, 8])
    self.assertEqual(ln2l(test_function(l2ln([2, 4, 3]), l2ln([0]))), [2, 4, 3])
    self.assertEqual(ln2l(test_function(l2ln([2, 4, 3]), l2ln([5, 6, 7]))), [7, 0, 1, 1])
    self.assertEqual(ln2l(test_function(l2ln([0]), l2ln([0]))), [0])
    self.assertEqual(ln2l(test_function(l2ln([9,9,9,9,9,9,9]), l2ln([9,9,9,9]))), [8,9,9,9,0,0,0,1])

class MyTest(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)

if __name__ == "__main__":
    unittest.main()