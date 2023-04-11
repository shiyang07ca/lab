"""

[1019] Next Greater Node In Linked List


You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.


Example 1:


Input: head = [2,1,5]
Output: [5,5,0]


Example 2:


Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]



Constraints:


	The number of nodes in the list is n.
	1 <= n <= 10⁴
	1 <= Node.val <= 10⁹

################################################################


# tag: Monotonic Stack


1019. 链表中的下一个更大节点

给定一个长度为 n 的链表 head

对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。

返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。


示例 1：

输入：head = [2,1,5]
输出：[5,5,0]


示例 2：

输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]


提示：

链表中节点数为 n
1 <= n <= 104
1 <= Node.val <= 109


"""

import sys
import inspect
import os
import unittest

from itertools import *
from collections import *
from copy import *
from typing import *
from math import *

from os.path import abspath, join, dirname

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

"""
作者：灵茶山艾府
链接：https://leetcode.cn/problems/next-greater-node-in-linked-list/solutions/2217563/tu-jie-dan-diao-zhan-liang-chong-fang-fa-v9ab/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

# 从右向左遍历
class Solution:
    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head = self.reverseList(head)
        ans = []
        st = []  # 单调栈（节点值）
        while head:
            while st and st[-1] <= head.val:
                st.pop()  # 弹出无用数据
            ans.append(st[-1] if st else 0)  # 栈顶就是第 i 个节点的下一个更大元素
            st.append(head.val)
            head = head.next
        return ans[::-1]  # 由于是倒着记录答案的，返回前要把答案反转


# 从左向右遍历
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        st = []  # 单调栈（节点值，节点下标）
        while head:
            while st and st[-1][0] < head.val:
                ans[st.pop()[1]] = head.val  # 用当前节点值更新答案
            st.append((head.val, len(ans)))  # 当前 ans 的长度就是当前节点的下标
            ans.append(0)  # 占位
            head = head.next
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
