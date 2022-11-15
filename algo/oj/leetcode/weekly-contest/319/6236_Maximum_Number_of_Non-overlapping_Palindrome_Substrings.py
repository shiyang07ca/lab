"""
6236. Maximum Number of Non-overlapping Palindrome Substrings
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.


Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.


################################################################

# TODO

6236. 不重叠回文子字符串的最大数目
给你一个字符串 s 和一个 正 整数 k 。

从字符串 s 中选出一组满足下述条件且 不重叠 的子字符串：

每个子字符串的长度 至少 为 k 。
每个子字符串是一个 回文串 。
返回最优方案中能选择的子字符串的 最大 数目。

子字符串 是字符串中一个连续的字符序列。

示例 1 ：

输入：s = "abaccdbbd", k = 3
输出：2
解释：可以选择 s = "abaccdbbd" 中斜体加粗的子字符串。"aba" 和 "dbbd" 都是回文，且长度至少为 k = 3 。
可以证明，无法选出两个以上的有效子字符串。


示例 2 ：

输入：s = "adbcda", k = 2
输出：0
解释：字符串中不存在长度至少为 2 的回文子字符串。


提示：

1 <= k <= s.length <= 2000
s 仅由小写英文字母组成


"""


"""
作者：endlesscheng
链接：https://leetcode.cn/problems/maximum-number-of-non-overlapping-palindrome-substrings/solution/zhong-xin-kuo-zhan-dppythonjavacgo-by-en-1yt1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

计算每个子串是否回文，可以用中心扩展法，思路参考 647. 回文子串 的 官方题解，下面只讲解 DP 部分。

定义 f[i] 表示 s[0..i-1] 中的不重叠回文子串的最大数目
特别地，定义 f[0] = 0 , 方便我们表示空字符串
如果 s[i] 不准回文子串中，那么有 f[i+1] = f[i]
采用中心扩展法，如果 s[l..r] 是回文子串，且 r-l+1>=k，那么有状态转移方程
            f[r + 1] = max(f[r+1], f[l] + 1)

最后答案为 f[n], 这里 n 为 s 的长度
代码实现时，由于长度为 x 的回文子串一定包含长为 x−2 的回文子串，所以回文子串的长
度达到 k 就可以退出循环了。

"""


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        f = [0] * (n + 1)
        for i in range(2 * n - 1):
            l, r = i // 2, i // 2 + i % 2  # 中心扩展法
            f[l + 1] = max(f[l + 1], f[l])
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 >= k:
                    f[r + 1] = max(f[r + 1], f[l] + 1)
                    break
                l -= 1
                r += 1
        return f[n]
