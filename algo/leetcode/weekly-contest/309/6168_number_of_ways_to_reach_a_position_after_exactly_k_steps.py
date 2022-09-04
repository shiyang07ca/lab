"""

6168. 恰好移动 k 步到达某一位置的方法数目


给你两个 正 整数 startPos 和 endPos 。最初，你站在 无限 数轴上位置 startPos 处。在一步移动中，你可以向左或者向右移动一个位置。

给你一个正整数 k ，返回从 startPos 出发、恰好 移动 k 步并到达 endPos 的 不同 方法数目。由于答案可能会很大，返回对 109 + 7 取余 的结果。

如果所执行移动的顺序不完全相同，则认为两种方法不同。

注意：数轴包含负整数。



示例 1：

输入：startPos = 1, endPos = 2, k = 3
输出：3
解释：存在 3 种从 1 到 2 且恰好移动 3 步的方法：
- 1 -> 2 -> 3 -> 2.
- 1 -> 2 -> 1 -> 2.
- 1 -> 0 -> 1 -> 2.
可以证明不存在其他方法，所以返回 3 。
示例 2：

输入：startPos = 2, endPos = 5, k = 10
输出：0
解释：不存在从 2 到 5 且恰好移动 10 步的方法。


提示：

1 <= startPos, endPos, k <= 1000

"""


class Solution:
    from functools import cache

    @cache
    def process(self, start, end, k):
        if start == end and k == 0:
            return 1
        if k == 0:
            return 0

        return self.process(start + 1, end, k - 1) + self.process(start - 1, end, k - 1)

    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        return self.process(startPos, endPos, k) % (10**9 + 7)
