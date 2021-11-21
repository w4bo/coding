import unittest
import os
from importlib import import_module
import time
from v1 import test_function
from v1 import ListNode

def list_2_listnode(l):
    head = ListNode(val=-1)
    res = head
    for i in range(len(l)):
        cur_node = ListNode(val=l[i])
        res.next = cur_node
        res = cur_node
    return head.next

def unit_test(self, f):
    self.assertEqual(f(list_2_listnode([2, 4, 3]), list_2_listnode([5, 6, 4])), list_2_listnode([7, 0, 8]))
    self.assertEqual(f(list_2_listnode([2, 4, 3]), list_2_listnode([0])), list_2_listnode([2, 4, 3]))
    self.assertEqual(f(list_2_listnode([2, 4, 3]), list_2_listnode([5, 6, 7])), list_2_listnode([7, 0, 1, 1]))
    self.assertEqual(f(list_2_listnode([0]), list_2_listnode([0])), list_2_listnode([0]))
    self.assertEqual(f(list_2_listnode([9,9,9,9,9,9,9]), list_2_listnode([9,9,9,9])), list_2_listnode([8,9,9,9,0,0,0,1]))

class MyTest(unittest.TestCase):
    def test(self):
        unit_test(self, test_function)

if __name__ == "__main__":
    unittest.main()