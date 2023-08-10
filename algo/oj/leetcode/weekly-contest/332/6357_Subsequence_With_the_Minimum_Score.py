"""

6357. Subsequence With the Minimum Score

You are given two strings s and t.

You are allowed to remove any number of characters from the string t.

The score string is 0 if no characters are removed from the string t, otherwise:

Let left be the minimum index among all removed characters.
Let right be the maximum index among all removed characters.
Then the score of the string is right - left + 1.

Return the minimum possible score to make t a subsequence of s.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abacaba", t = "bzaa"
Output: 1
Explanation: In this example, we remove the character "z" at index 1 (0-indexed).
The string t becomes "baa" which is a subsequence of the string "abacaba" and the score is 1 - 1 + 1 = 1.
It can be proven that 1 is the minimum score that we can achieve.
Example 2:

Input: s = "cde", t = "xyz"
Output: 3
Explanation: In this example, we remove characters "x", "y" and "z" at indices 0, 1, and 2 (0-indexed).
The string t becomes "" which is a subsequence of the string "cde" and the score is 2 - 0 + 1 = 3.
It can be proven that 3 is the minimum score that we can achieve.


Constraints:

1 <= s.length, t.length <= 105
s and t consist of only lowercase English letters.


################################################################

https://leetcode.cn/contest/weekly-contest-332/problems/subsequence-with-the-minimum-score/

# TODO



6357. 最少得分子序列

给你两个字符串 s 和 t 。

你可以从字符串 t 中删除任意数目的字符。

如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：

令 left 为删除字符中的最小下标。
令 right 为删除字符中的最大下标。
字符串的得分为 right - left + 1 。

请你返回使 t 成为 s 子序列的最小得分。

一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 "ace" 是 "abcde" 的子序列，但是 "aec" 不是）。



示例 1：

输入：s = "abacaba", t = "bzaa"
输出：1
解释：这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
1 是能得到的最小得分。


示例 2：

输入：s = "cde", t = "xyz"
输出：3
解释：这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
3 是能得到的最小得分。


提示：

1 <= s.length, t.length <= 105

"""


"""

"""


"""
作者：endlesscheng
链接：https://leetcode.cn/problems/subsequence-with-the-minimum-score/solution/qian-hou-zhui-fen-jie-san-zhi-zhen-pytho-6cmr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

前后缀分解+双指针

提示 1
在 [left,right] 之间的字符，删除是不影响得分的，且删除后更有机会让剩余部分是 s
的子序列。因此只需考虑删除的是 t 的子串，而不是子序列。


提示 2
删除子串后，剩余部分是 t 的一个前缀和一个后缀。
假设前缀匹配的是 s 的一个前缀s[:i]，后缀匹配的是s 的一个后缀s[i:]。这里匹配指子
序列匹配。
那么枚举 i，分别计算能够与 s[:i] 和 s[i:] 匹配的t 的最长前缀和最长后缀，就知道要
删除的子串的最小值了。这个技巧叫做「前后缀分解」。


提示 3
具体来说：

定义 pre[i] 为 s[:i] 对应的 t 的最长前缀的结束下标。
定义 suf[i] 为 s[i:] 对应的 t 的最长后缀的开始下标。
那么删除的子串就是从 pre[i]+1 到 suf[i]−1 这段，答案就是 suf[i]−pre[i]−1 的最小
值。

代码实现时，可以先计算 suf，然后一边计算 pre，一边更新最小值，所以 pre 可以省略。

"""


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        suf = [m] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            suf[i] = j + 1
        ans = suf[0]  # 删除 t[:suf[0]]
        if ans == 0:
            return 0

        j = 0
        for i, c in enumerate(s):
            if c == t[j]:  # 注意 j 不会等于 m，因为上面 suf[0]>0 表示 t 不是 s 的子序列
                j += 1
                ans = min(ans, suf[i + 1] - j)  # 删除 t[j:suf[i+1]]
        return ans
