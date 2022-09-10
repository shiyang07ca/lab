"""

# TODO

[32] Longest Valid Parentheses


Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


--------------------------------------------------

Example 1:


Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".


--------------------------------------------------

Example 2:


Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".


--------------------------------------------------

Example 3:


Input: s = ""
Output: 0



Constraints:


	0 <= s.length <= 3 * 10⁴
	s[i] is '(', or ')'.

################################################################


32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。



示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"


示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"


示例 3：

输入：s = ""
输出：0


提示：

0 <= s.length <= 3 * 104
s[i] 为 '(' 或 ')'


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


class Solution:
    """
    对于遇到的每个 '(' ，我们将它的下标放入栈中
    对于遇到的每个 ')' ，我们先弹出栈顶元素表示匹配了当前右括号：
    如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来
    更新我们之前提到的「最后一个没有被匹配的右括号的下标」
    如果栈不为空，当前右括号的下标减去栈顶元素即为
    「以该右括号为结尾的最长有效括号的长度」

    作者：LeetCode-Solution
    链接：https://leetcode.cn/problems/longest-valid-parentheses/solution/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    """

    def s1(self, s):
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                else:
                    stack.append(i)

        return ans

    def s2(self, s):
        if not s:
            return 0

        N = len(s)
        # dp[i] 表示以 s[i] 结尾的，最长有效括号长度
        dp = [0] * N
        stack = []
        for i in range(N):
            if s[i] == "(":
                stack.append(s[i])
            else:  # ')'
                if stack:
                    stack.pop()
                    pair_count = 2 + dp[i - 1]
                    # 查看当前有效括号长度之前的 dp 数组结果
                    pre_index = i - pair_count
                    if pre_index > 0:
                        pair_count += dp[pre_index]
                    dp[i] = pair_count

        return max(dp)

    def longestValidParentheses(self, s: str) -> int:
        # return self.s1(s)

        return self.s2(s)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        s = "()(())"
        self.assertEqual(
            self.sl.longestValidParentheses(s),
            6,
        )
        print("################")

    def test_sl2(self):
        s = "()(()"
        self.assertEqual(
            self.sl.longestValidParentheses(s),
            2,
        )
        print("################")

    def test_sl3(self):
        s = ")()())"
        self.assertEqual(
            self.sl.longestValidParentheses(s),
            4,
        )
        print("################")

    def test_sl4(self):
        s = "(()"
        self.assertEqual(
            self.sl.longestValidParentheses(s),
            2,
        )
        print("################")

    def test_sl5(self):
        s = ")()())"
        self.assertEqual(
            self.sl.longestValidParentheses(s),
            4,
        )
        print("################")


if __name__ == "__main__":
    unittest.main()
