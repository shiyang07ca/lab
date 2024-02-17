"""

给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的长度，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。



示例 1：

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
示例 2：

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。


提示：

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] 仅由 '0' 和 '1' 组成
1 <= m, n <= 100


"""
from typing import List


class Solution:

    from functools import cache

    @cache
    def recur(self, m, n, strs, ans):
        if not strs:
            return ans

        c_0 = strs[0].count("0")
        c_1 = strs[0].count("1")
        if c_0 <= m and c_1 <= n:
            return max(
                self.recur(m, n, strs[1:], ans),
                self.recur(m - c_0, n - c_1, strs[1:], ans + 1),
            )
        else:
            return self.recur(m, n, strs[1:], ans)

    def dp(self, m, n, strs):
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            c0 = s.count("0")
            c1 = s.count("1")
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    dp[i][j] = max(dp[i - c0][j - c1] + 1, dp[i][j])

        return dp[m][n]

    # * 错误的尝试*
    def dp1(self, m, n, strs):
        c0 = [s.count("0") for s in strs]
        c1 = [s.count("1") for s in strs]
        dp_m = [[0] * (m + 1) for _ in range(len(strs))]
        dp_n = [[0] * (n + 1) for _ in range(len(strs))]

        # print(c0, c1, dp_m, dp_n)
        for i in range(len(dp_m)):
            for j in range(len(dp_m[0])):
                print(i, j)
                if j >= c0[i]:
                    dp_m[i][j] = 1

                if i > 0 and j >= c0[i]:
                    dp_m[i][j] += max([dp_m[s][j - c0[i]] for s in range(0, i)])

            print("m")
            [print(mm) for mm in dp_m]

        for i in range(len(dp_n)):
            for j in range(len(dp_n[0])):
                if j >= c1[i]:
                    dp_n[i][j] = 1

                if i > 0 and j >= c1[i]:
                    dp_n[i][j] += max([dp_n[s][j - c1[i]] for s in range(0, i)])

            print("n")
            [print(mm) for mm in dp_n]

        # print("m: ", dp_m)
        # print("n: ", dp_n)
        ans = 0
        for i in range(len(strs)):
            ansi = min(dp_m[i][m], dp_n[i][n])
            ans = max(ans, ansi)
        return ans

        # return min(dp_m[len(strs) - 1][m], dp_n[len(strs) - 1][n])

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # return self.recur(m, n, tuple(strs), 0)
        return self.dp(m, n, strs)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        s = ["10", "0001", "111001", "1", "0"]
        m = 5
        n = 3
        ans = 4
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = ["10", "0", "1"]
        m = 1
        n = 1
        ans = 2
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = ["10", "0001", "111001", "1", "0"]
        m = 4
        n = 3
        ans = 3
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = ["111", "1000", "1000", "1000"]
        m = 9
        n = 3
        ans = 3
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)

        s = [
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
            "1",
            "0",
        ]
        m = 30
        n = 30
        ans = 47
        self.assertEqual(self.sl.findMaxForm(s, m, n), ans)


if __name__ == "__main__":
    unittest.main()
