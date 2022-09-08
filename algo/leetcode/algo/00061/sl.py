"""

[61] Rotate List


Given the head of a linked list, rotate the list to the right by k places.


--------------------------------------------------

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]


--------------------------------------------------

Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]



Constraints:


	The number of nodes in the list is in the range [0, 500].
	-100 <= Node.val <= 100
	0 <= k <= 2 * 10⁹

################################################################


61. 旋转链表


给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。


示例 1：

           1 2 3 4 5
rotate1    2 3 4 5 1
rotate2    4 5 1 2 3


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]


示例 2：
         0  1  2

r1       2  0  1
r2       1  2  0
r3       0  1  2
r4       2  0  1

输入：head = [0,1,2], k = 4
输出：[2,0,1]


提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109


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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        cur, size = head, 0
        while cur is not None:
            cur = cur.next
            size += 1
        k = k % size
        if k == 0:
            return head

        fast, slow = head, head
        while k > 0:
            fast = fast.next
            if fast is None:
                fast = head
            k -= 1
        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        ans = slow.next
        fast.next = head
        slow.next = None
        return ans


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
