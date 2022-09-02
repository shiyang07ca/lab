"""

[206] Reverse Linked List


Given the head of a singly linked list, reverse the list, and return the reversed list.


--------------------------------------------------

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]


--------------------------------------------------

Example 2:


Input: head = [1,2]
Output: [2,1]


--------------------------------------------------

Example 3:


Input: head = []
Output: []



Constraints:


	The number of nodes in the list is the range [0, 5000].
	-5000 <= Node.val <= 5000



Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

################################################################

206. 反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。


示例 1：

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：

输入：head = [1,2]
输出：[2,1]
示例 3：

输入：head = []
输出：[]


提示：

链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000


进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_iter(self, head):
        if not head or not head.next:
            return head

        pre = None
        while head:
            cur = head
            head = head.next
            cur.next = pre
            pre = cur

        return pre

    def reverse_recur(self, head):
        if not head or not head.next:
            return head

        last = self.reverse_recur(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # return self.reverse_iter(head)
        return self.reverse_recur(head)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
