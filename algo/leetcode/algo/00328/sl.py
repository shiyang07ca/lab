"""

[328] Odd Even Linked List


Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.


--------------------------------------------------

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]


--------------------------------------------------

Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]



Constraints:


	The number of nodes in the linked list is in the range [0, 10⁴].
	-10⁶ <= Node.val <= 10⁶


################################################################



328. 奇偶链表
给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。



示例 1:
  1 ->  2  ->  3   ->  4  ->  5
             |
             v
  1 ->  3  ->  5   ->  2  ->  4


输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]


示例 2:

输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]

提示:

n ==  链表中的节点数
0 <= n <= 104
-106 <= Node.val <= 106

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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head

        l, r = head, head.next
        dummyL, dummyR = ListNode(-1), ListNode(-1)
        dummyL.next = l
        dummyR.next = r
        while r is not None and r.next is not None:
            r1 = r.next
            r2 = r.next.next
            l.next = r1
            r.next = r2
            l = r1
            r = r2

        l.next = dummyR.next
        return dummyL.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl1(self):
        arr = [1, 2, 3, 4, 5]
        head = build_from_array(arr)
        print(head)
        res = self.sl.oddEvenList(head)
        print(res)
        print('################')

    def test_sl2(self):
        arr = [1, 2, 3, 4]
        head = build_from_array(arr)
        print(head)
        res = self.sl.oddEvenList(head)
        print(res)
        print('################')

    def test_sl3(self):
        arr = [2, 1, 3, 5, 6, 4, 7]
        head = build_from_array(arr)
        print(head)
        res = self.sl.oddEvenList(head)
        print(res)
        print('################')


if __name__ == "__main__":
    unittest.main()
