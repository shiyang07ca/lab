"""

[24] Swap Nodes in Pairs


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


--------------------------------------------------

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]


--------------------------------------------------

Example 2:


Input: head = []
Output: []


--------------------------------------------------

Example 3:


Input: head = [1]
Output: [1]



Constraints:


	The number of nodes in the list is in the range [0, 100].
	0 <= Node.val <= 100

################################################################

24. 两两交换链表中的节点
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。



示例 1：

   1  ->  2  ->  3  -> 4
            |
            v
   2  ->  1  ->  4  -> 3

输入：head = [1,2,3,4]
输出：[2,1,4,3]


示例 2：

输入：head = []
输出：[]


示例 3：

输入：head = [1]
输出：[1]


提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100

"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *
from algo.data_structure.linkedlist import ListNode, build_from_array


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        dummy = ListNode(-1)
        dummy.next = head

        left, right = head, head.next
        pre = dummy
        while left and right:
            rightNext = right.next
            right.next = left
            left.next = rightNext
            pre.next = right

            pre = left
            left = left.next
            if left and left.next:
                right = left.next
            else:
                break

        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl1(self):
        arr = [1, 2, 3, 4]
        head = build_from_array(arr)
        # print(head)
        res = self.sl.swapPairs(head)
        print(res)

    def test_sl2(self):
        arr = []
        head = build_from_array(arr)

        res = self.sl.swapPairs(head)
        print(res)

    def test_sl3(self):
        arr = [1]
        head = build_from_array(arr)
        res = self.sl.swapPairs(head)
        print(res)

    def test_sl4(self):
        arr = [1, 2, 3]
        head = build_from_array(arr)
        # print(head)
        res = self.sl.swapPairs(head)
        print(res)


if __name__ == "__main__":
    unittest.main()
