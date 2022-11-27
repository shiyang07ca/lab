"""

6246. Append Characters to String to Make Subsequence

You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.


Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.

################################################################

6246. 追加字符以获得子序列

给你两个仅由小写英文字母组成的字符串 s 和 t 。

现在需要通过向 s 末尾追加字符的方式使 t 变成 s 的一个 子序列 ，返回需要追加的最少字符数。

子序列是一个可以由其他字符串删除部分（或不删除）字符但不改变剩下字符顺序得到的字符串。



示例 1：

输入：s = "coaching", t = "coding"
输出：4
解释：向 s 末尾追加字符串 "ding" ，s = "coachingding" 。
现在，t 是 s ("coachingding") 的一个子序列。
可以证明向 s 末尾追加任何 3 个字符都无法使 t 成为 s 的一个子序列。


示例 2：

输入：s = "abcde", t = "a"
输出：0
解释：t 已经是 s ("abcde") 的一个子序列。


示例 3：

输入：s = "z", t = "abcde"
输出：5
解释：向 s 末尾追加字符串 "abcde" ，s = "zabcde" 。
现在，t 是 s ("zabcde") 的一个子序列。
可以证明向 s 末尾追加任何 4 个字符都无法使 t 成为 s 的一个子序列。


提示：

1 <= s.length, t.length <= 105
s 和 t 仅由小写英文字母组成

"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # f[i] 表示前 i 个字符最长匹配 t 的子序列长度
        # f[i+1] = f[i] +  1  if t[f[i]] == c
        # 返回 len(t) - f[len(s)]
        f = [0] * (10**5 + 10)
        for i, c in enumerate(s, 1):
            if f[i - 1] < len(t) and t[f[i - 1]] == c:
                f[i] += 1
            f[i] += f[i - 1]
        return len(t) - f[len(s)]


"""

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/D1fgh9/view/LGcCHr/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

只需要使用 s 对 t 进行贪心匹配，一旦遇到相同字母即匹配下一项，直至完全遍历 s，剩
下没有匹配的 t 中字符数量即为答案。

"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for char in s:
            if i < len(t) and char == t[i]:
                i += 1
        return len(t) - i
