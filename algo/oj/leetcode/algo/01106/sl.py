"""

[1106] Parsing A Boolean Expression


A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:


	't' that evaluates to true.
	'f' that evaluates to false.
	'!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
	'&(subExpr₁, subExpr₂, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr₁, subExpr₂, ..., subExprn where n >= 1.
	'|(subExpr₁, subExpr₂, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr₁, subExpr₂, ..., subExprn where n >= 1.


Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.


Example 1:


Input: expression = "&(|(f))"
Output: false
Explanation:
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.


Example 2:


Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.


Example 3:


Input: expression = "!(&(f,t))"
Output: true
Explanation:
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.



Constraints:


	1 <= expression.length <= 2 * 10⁴
	expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

################################################################


# TODO
# tag: stack

1106. 解析布尔表达式
给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。

有效的表达式需遵循以下约定：

"t"，运算结果为 True
"f"，运算结果为 False
"!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
"&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
"|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）


示例 1：

输入：expression = "!(f)"
输出：true


示例 2：

输入：expression = "|(f,t)"
输出：true


示例 3：

输入：expression = "&(t,f)"
输出：false


示例 4：

输入：expression = "|(&(t,f,t),!(t))"
输出：false


提示：

1 <= expression.length <= 20000
expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
expression 是以上述形式给出的有效表达式，表示一个布尔值。


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from itertools import *
from collections import *

from typing import *

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

https://leetcode.cn/problems/parsing-a-boolean-expression/solution/by-lcbin-ys8t/

"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = "!&|tf"
        st = []
        for c in expression:
            # print(st)
            if c in s:
                st.append(c)
            elif c == ")":
                t = f = 0
                # print(st, c)
                while st[-1] in ["t", "f"]:
                    if st[-1] == "t":
                        t += 1
                    elif st[-1] == "f":
                        f += 1
                    st.pop()
                # 此时栈顶一定是运算符
                op = st.pop()
                if op == "!":
                    tmp = "f" if t else "t"
                elif op == "&":
                    tmp = "f" if f else "t"
                elif op == "|":
                    tmp = "t" if t else "f"
                st.append(tmp)
        print(st)
        return st[-1] == "t"


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        expression = "!(f)"
        self.assertEqual(
            self.sl.parseBoolExpr(expression),
            True,
        )

        expression = "|(f,t)"
        self.assertEqual(
            self.sl.parseBoolExpr(expression),
            True,
        )

        expression = "&(t,f)"
        self.assertEqual(
            self.sl.parseBoolExpr(expression),
            False,
        )

        expression = "|(&(t,f,t),!(t))"
        self.assertEqual(
            self.sl.parseBoolExpr(expression),
            False,
        )

        expression = "!(&(f,t))"
        self.assertEqual(
            self.sl.parseBoolExpr(expression),
            True,
        )


if __name__ == "__main__":
    unittest.main()
