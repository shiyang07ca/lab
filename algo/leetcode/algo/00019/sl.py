"""

[19] Remove Nth Node From End of List


Given the head of a linked list, remove the nth node from the end of the list and return its head.


--------------------------------------------------

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


--------------------------------------------------

Example 2:


Input: head = [1], n = 1
Output: []


--------------------------------------------------

Example 3:


Input: head = [1,2], n = 1
Output: [1]



Constraints:


	The number of nodes in the list is sz.
	1 <= sz <= 30
	0 <= Node.val <= 100
	1 <= n <= sz



Follow up: Could you do this in one pass?


################################################################


19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。



示例 1：
  1  ->  2  ->  3  -> 4  ->  5
            |
            V
  1  ->  2  ->  3    ---->   5

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]


示例 2：

输入：head = [1], n = 1
输出：[]


示例 3：

输入：head = [1,2], n = 1
输出：[1]


提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


进阶：你能尝试使用一趟扫描实现吗？

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
    def findNthFromEnd(self, head, n):
        p1 = p2 = head

        # p1 先走 n 步，还差 sz - n 步到达终点
        while n > 0:
            p1 = p1.next
            n -= 1

        # p1，p2 同时走，当 p1 来到最后节点时，p2 来到倒数第 n 个节点
        preNode = p2
        while p1 is not None:
            p1 = p1.next
            preNode = p2
            p2 = p2.next

        return p2, preNode

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 虚拟节点
        dummyNode = ListNode(-1)
        dummyNode.next = head
        node, preNode = self.findNthFromEnd(dummyNode, n)
        preNode.next = node.next

        return dummyNode.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl1(self):
        arr = [1, 2, 3, 4, 5]
        n = 2
        head = build_from_array(arr)
        res = self.sl.removeNthFromEnd(head, n)
        print(res)

        arr = [1]
        n = 1
        head = build_from_array(arr)
        res = self.sl.removeNthFromEnd(head, n)
        print(res)

        arr = [1, 2]
        n = 1
        head = build_from_array(arr)
        res = self.sl.removeNthFromEnd(head, n)
        print(res)


if __name__ == "__main__":
    unittest.main()
