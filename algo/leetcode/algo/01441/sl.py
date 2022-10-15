"""

[1441] Build an Array With Stack Operations


You are given an integer array target and an integer n.

You have an empty stack with the two following operations:


	"Push": pushes an integer to the top of the stack.
	"Pop": removes the integer on the top of the stack.


You also have a stream of the integers in the range [1, n].

Use the two stack operations to make the numbers in the stack (from the bottom to the top) equal to target. You should follow the following rules:


	If the stream of the integers is not empty, pick the next integer from the stream and push it to the top of the stack.
	If the stack is not empty, pop the integer at the top of the stack.
	If, at any moment, the elements in the stack (from the bottom to the top) are equal to target, do not read new integers from the stream and do not do more operations on the stack.


Return the stack operations needed to build target following the mentioned rules. If there are multiple valid answers, return any of them.


Example 1:


Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Pop the integer on the top of the stack. s = [1].
Read 3 from the stream and push it to the stack. s = [1,3].


Example 2:


Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Read 3 from the stream and push it to the stack. s = [1,2,3].


Example 3:


Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: Initially the stack s is empty. The last element is the top of the stack.
Read 1 from the stream and push it to the stack. s = [1].
Read 2 from the stream and push it to the stack. s = [1,2].
Since the stack (from the bottom to the top) is equal to target, we stop the stack operations.
The answers that read integer 3 from the stream are not accepted.



Constraints:


	1 <= target.length <= 100
	1 <= n <= 100
	1 <= target[i] <= n
	target is strictly increasing.


################################################################


1441. 用栈操作构建数组
给你一个数组 target 和一个整数 n。每次迭代，需要从  list = { 1 , 2 , 3 ..., n } 中依次读取一个数字。

请使用下述操作来构建目标数组 target ：

"Push"：从 list 中读取一个新元素， 并将其推入数组中。
"Pop"：删除数组中的最后一个元素。
如果目标数组构建完成，就停止读取更多元素。
题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。

请返回构建目标数组所用的操作序列。如果存在多个可行方案，返回任一即可。


示例 1：

输入：target = [1,3], n = 3
输出：["Push","Push","Pop","Push"]
解释：
读取 1 并自动推入数组 -> [1]
读取 2 并自动推入数组，然后删除它 -> [1]
读取 3 并自动推入数组 -> [1,3]

示例 2：

输入：target = [1,2,3], n = 3
输出：["Push","Push","Push"]

示例 3：

输入：target = [1,2], n = 4
输出：["Push","Push"]
解释：只需要读取前 2 个数字就可以停止。


提示：

1 <= target.length <= 100
1 <= n <= 100
1 <= target[i] <= n
target 严格递增


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


class Solution1:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if not target:
                return ans

            if target[0] == i:
                ans.append("Push")
                target.pop(0)
            else:
                ans.append("Push")
                ans.append("Pop")

        return ans


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        cur = 1
        for t in target:
            d = t - cur

            if d == 0:
                ans.append("Push")
                cur += 1
            else:
                ans.extend(["Push", "Pop"] * d)
                ans.append("Push")
                cur = t + 1
        # for _ in range(cur, n+ 1):
        #     ans.append("Push")
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        t = [1, 3]
        n = 3
        self.assertEqual(
            self.sl.buildArray(t, n),
            ["Push", "Push", "Pop", "Push"],
        )

        t = [1, 2, 3]
        n = 3
        self.assertEqual(self.sl.buildArray(t, n), ["Push", "Push", "Push"])

        t = [1, 2]
        n = 4
        self.assertEqual(self.sl.buildArray(t, n), ["Push", "Push"])

        t = [2, 3, 4]
        n = 4
        self.assertEqual(
            self.sl.buildArray(t, n), ["Push", "Pop", "Push", "Push", "Push"]
        )


if __name__ == "__main__":
    unittest.main()
