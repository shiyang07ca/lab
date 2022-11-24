"""

6244. Number of Beautiful Partitions

You are given a string s that consists of the digits '1' to '9' and two integers k and minLength.

A partition of s is called beautiful if:

s is partitioned into k non-intersecting substrings.
Each substring has a length of at least minLength.
Each substring starts with a prime digit and ends with a non-prime digit. Prime digits are '2', '3', '5', and '7', and the rest of the digits are non-prime.
Return the number of beautiful partitions of s. Since the answer may be very large, return it modulo 109 + 7.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "23542185131", k = 3, minLength = 2
Output: 3
Explanation: There exists three ways to create a beautiful partition:
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"
Example 2:

Input: s = "23542185131", k = 3, minLength = 3
Output: 1
Explanation: There exists one way to create a beautiful partition: "2354 | 218 | 5131".
Example 3:

Input: s = "3312958", k = 3, minLength = 1
Output: 1
Explanation: There exists one way to create a beautiful partition: "331 | 29 | 58".


Constraints:

1 <= k, minLength <= s.length <= 1000
s consists of the digits '1' to '9'.

################################################################

# TODO
# tag: dp, PrefixSum


6244. 完美分割的方案数 显示英文描述

给你一个字符串 s ，每个字符是数字 '1' 到 '9' ，再给你两个整数 k 和 minLength 。

如果对 s 的分割满足以下条件，那么我们认为它是一个 完美 分割：

- s 被分成 k 段互不相交的子字符串。
- 每个子字符串长度都 至少 为 minLength 。
- 每个子字符串的第一个字符都是一个 质数 数字，最后一个字符都是一个 非质数 数字。质
  数数字为 '2' ，'3' ，'5' 和 '7' ，剩下的都是非质数数字。

请你返回 s 的 完美 分割数目。由于答案可能很大，请返回答案对 109 + 7 取余 后的结果。

一个 子字符串 是字符串中一段连续字符串序列。


示例 1：

输入：s = "23542185131", k = 3, minLength = 2
输出：3
解释：存在 3 种完美分割方案：
"2354 | 218 | 5131"
"2354 | 21851 | 31"
"2354218 | 51 | 31"


示例 2：

输入：s = "23542185131", k = 3, minLength = 3
输出：1
解释：存在一种完美分割方案："2354 | 218 | 5131" 。


示例 3：

输入：s = "3312958", k = 3, minLength = 1
输出：1
解释：存在一种完美分割方案："331 | 29 | 58" 。


提示：

1 <= k, minLength <= s.length <= 1000
s 每个字符都为数字 '1' 到 '9' 之一。

"""

""""""

"""

作者：endlesscheng
链接：https://leetcode.cn/problems/number-of-beautiful-partitions/solution/dong-tai-gui-hua-jian-ji-xie-fa-xun-huan-xyw3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


定义 f[i][j] 表示把 s 的前 j 个字符分割成 i 段的方案数（每段需要满足题目的后两个要求）。

定义 j 为分割点，等价于 s[j] 不是质数且 s[j+1] 是质数。

如果 j 是分割点，那么可以考虑枚举第 i−1 段与第 i 段的分割点 j' ，需满足 j-j'  ≥ minLength。

累加所有 f[i−1][j′]，记作 sum，那么 f[i][j]=sum。

每个 f[i][j] 都要这样累加就太慢了，需要优化。

我们可以从小到大同时遍历 j' 和 j，一边更新 sum，一边计算 f[i][j]，具体见代码。

为方便计算，定义初始值 f[0][0]=1，表示空串的 0 个分割算作一种方案。因为这个原因，
要把所有下标 j 向后移动一位。

答案为 f[k][n]，这里 n 为 s 的长度。

还有一些剪枝和循环次数优化的小技巧，具体见代码。


"""

"""

如何思考动态规划？

1. 问题中有那些变量？
分割的个数 k
字符串的长度 n

2. 重新复述一遍问题，替换变量名
把一个长度为 j 的字符串，分割出 i 段的合法方案数

3. （关键）最后一步发生了什么
分割出 一个 子串
长度为 x
且这子串是 s 的一个后缀

4. 去掉最后一步，问题规模缩小了，变成什么样了？
把一个长度为 j - x 的字符串，分割出 i-1 段的合法方案数

5. 得到状态转移方程
2 => f[i][j] 表示把 s 的前 j 个字符分割成 i 段的合法方案数
4 => f[i][j] += f[i-1][j']  j' 是第 i 段的结束下标
     枚举 j'
     j' - j + 1 >= minLength
     s[j] 是质数 s[j'] 不是质数

6. 初始值和答案
f[0][0] = 1
ans = f[k][n]

7. 优化转移
j 变大的时候，j' 也在变大
前缀和优化 += 枚举 j'

"""


class Solution:
    def beautifulPartitions(self, s: str, k: int, l: int) -> int:
        MOD = 10**9 + 7

        def is_prime(c: str) -> bool:
            return c in "2357"

        # 判断是否可以在 j-1 和 j 之间分割（开头和末尾也算）
        def can_partition(j: int) -> bool:
            return j == 0 or j == n or not is_prime(s[j - 1]) and is_prime(s[j])

        n = len(s)
        if k * l > n or not is_prime(s[0]) or is_prime(s[-1]):  # 剪枝
            return 0
        f = [[0] * (n + 1) for _ in range(k + 1)]
        f[0][0] = 1
        for i in range(1, k + 1):
            sum = 0
            # 优化：枚举的起点和终点需要给前后的子串预留出足够的长度
            for j in range(i * l, n - (k - i) * l + 1):
                if can_partition(j - l):
                    sum = (sum + f[i - 1][j - l]) % MOD  # j'=j-l 双指针
                if can_partition(j):
                    f[i][j] = sum
        return f[k][n]


"""

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/bb9NEI/view/kdE1WZ/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


注意到分割的位置是确定的，我们先对其进行预处理。

而我们使用从 i 位置后分割 xx 次这两变量作为状态变量。

状态转移我们进行分类讨论：

1. i 位置进行分割：我们可以直接找到下一个可能分割的节点（由于 MinLengthMinLength 的
存在），由于前面处理数组的单调性，我们可以二分解决。
2. i 位置不进行分割：我们直接讨论下一个节点。
两种情况加总即为所求。

注意边界条件为已经拆分了 k-1 次与已经到数组尾端而未分割足够次数。还要注意，开头
讨论原数组的第一项与最后一项也应当满足对应条件，否则输出 0.

"""

mod = 10**9 + 7
primes = {"2", "3", "5", "7"}


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        if s[0] not in primes or s[-1] in primes:
            return 0
        splits = []
        n = len(s)
        for i in range(minLength - 1, n - minLength):
            if s[i] not in primes and s[i + 1] in primes:
                splits.append(i)

        @cache
        def getRes(idx, used):
            if used == k - 1:
                return 1
            if idx >= len(splits):
                return 0
            return (
                getRes(idx + 1, used)
                + getRes(bisect_left(splits, splits[idx] + minLength), used + 1)
            ) % mod

        ans = getRes(0, 0)
        getRes.cache_clear()
        return ans


# 用时为 600ms，我们也可以进行剪枝，在后续每个分割位置都选的情况下，仍然不
# 能选出 k−1 个分割点时，进行直接返回 00.


mod = 10**9 + 7
primes = {"2", "3", "5", "7"}


class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        if s[0] not in primes or s[-1] in primes:
            return 0
        splits = []
        n = len(s)
        for i in range(minLength - 1, n - minLength):
            if s[i] not in primes and s[i + 1] in primes:
                splits.append(i)

        @cache
        def getRes(idx, used):
            if used == k - 1:
                return 1
            if idx >= len(splits):
                return 0
            if used + len(splits) - idx < k - 1:
                return 0
            return (
                getRes(idx + 1, used)
                + getRes(bisect_left(splits, splits[idx] + minLength), used + 1)
            ) % mod

        ans = getRes(0, 0)
        getRes.cache_clear()
        return ans
