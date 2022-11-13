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
