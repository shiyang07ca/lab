"""

[1138] Alphabet Board Path


On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].

Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.



We may make the following moves:


	'U' moves our position up one row, if the position exists on the board;
	'D' moves our position down one row, if the position exists on the board;
	'L' moves our position left one column, if the position exists on the board;
	'R' moves our position right one column, if the position exists on the board;
	'!' adds the character board[r][c] at our current position (r, c) to the answer.


(Here, the only positions that exist on the board are positions with letters on them.)

Return a sequence of moves that makes our answer equal to target in the minimum number of moves.  You may return any path that does so.


Example 1:
Input: target = "leet"
Output: "DDR!UURRR!!DDD!"
Example 2:
Input: target = "code"
Output: "RR!DDRR!UUL!R!"


Constraints:


	1 <= target.length <= 100
	target consists only of English lowercase letters.

################################################################

1138. 字母板上的路径

我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。

在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。

我们可以按下面的指令规则行动：

如果方格存在，'U' 意味着将我们的位置上移一行；
如果方格存在，'D' 意味着将我们的位置下移一行；
如果方格存在，'L' 意味着将我们的位置左移一列；
如果方格存在，'R' 意味着将我们的位置右移一列；
'!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
（注意，字母板上只存在有字母的位置。）

返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。



示例 1：

输入：target = "leet"
输出："DDR!UURRR!!DDD!"


示例 2：

输入：target = "code"
输出："RR!DDRR!UUL!R!"


提示：

1 <= target.length <= 100
target 仅含有小写英文字母。


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


# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/alphabet-board-path/solution/zhu-yi-z-de-wei-zhi-pythonjavacgo-by-end-1ha7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ans = []
        x = y = 0
        for c in target:
            nx, ny = divmod(ord(c) - ord("a"), 5)  # 目标位置
            v = "UD"[nx > x] * abs(nx - x)  # 竖直
            h = "LR"[ny > y] * abs(ny - y)  # 水平
            ans.append((v + h if c != "z" else h + v) + "!")
            x, y = nx, ny
        return "".join(ans)


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
