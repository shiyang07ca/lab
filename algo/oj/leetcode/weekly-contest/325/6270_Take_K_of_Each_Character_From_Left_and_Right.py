"""
6270. Take K of Each Character From Left and Right

You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.



Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation:
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.


Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length

################################################################

# TODO

6270. 每种字符至少取 K 个

给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。

你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。



示例 1：

输入：s = "aabaaaacaabc", k = 2
输出：8
解释：
从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
共需要 3 + 5 = 8 分钟。
可以证明需要的最少分钟数是 8 。


示例 2：

输入：s = "a", k = 1
输出：-1
解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。


提示：

1 <= s.length <= 105
s 仅由字母 'a'、'b'、'c' 组成
0 <= k <= s.length

"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/solution/on-shuang-zhi-zhen-by-endlesscheng-4g9p/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

设从左侧取到第 i 个字符，从右侧取到第 j 个字符。

由于随着 i 的变大，j 也会单调变大，因此可以用双指针，一边从小到大枚举 i，一边维
护 j 的最大位置（j 尽量向右移）。

对于左侧没有取字符的情况需要单独计算。

"""


# 双指针
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # 字符串 = 前缀 + 后缀
        # 枚举前缀的长度
        # 前缀为空：从右向左遍历，找到最短的满足要求的后缀
        # 前缀不为空：枚举
        #
        # aabaaaacaabc  k = 2
        #      baaaacaabc
        # a    baaaacaabc
        # aa   baaaacaabc
        # aab       caabc
        # aaba      caabc

        j = n = len(s)
        c = Counter()
        while c["a"] < k or c["b"] < k or c["c"] < k:
            if j == 0:
                return -1
            j -= 1
            c[s[j]] += 1
        ans = n - j  # 左侧没有取字符
        for i, ch in enumerate(s):
            c[ch] += 1
            while j < n and c[s[j]] > k:  # 维护 j 的最大下标
                c[s[j]] -= 1
                j += 1
            ans = min(ans, i + 1 + n - j)
            if j == n:
                break
        return ans


# 双指针
"""

滑动窗口，可以将两个原字符串拼接，接下来只要维持左端点不越过初始位置即可。由于字
符集很小，我们滑动窗口每次更新时判断是否有足够多字符即可。

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/RmydJj/view/cYCjYk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def checkCounter(cnt):
            for char in "abc":
                if cnt[char] < k:
                    return False
            return True

        n = len(s)
        tmp = s * 2
        l, r = 0, n
        cnt = Counter(s)
        if not checkCounter(cnt):
            return -1
        ans = n
        while l <= n:
            while not checkCounter(cnt):
                cnt[tmp[r]] += 1
                r += 1
            ans = min(ans, r - l)
            cnt[tmp[l]] -= 1
            l += 1
        return ans
