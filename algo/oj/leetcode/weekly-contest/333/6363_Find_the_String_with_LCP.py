"""

6363. Find the String with LCP

We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.



Example 1:

Input: lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
Output: "abab"
Explanation: lcp corresponds to any 4 letter string with two alternating letters. The lexicographically smallest of them is "abab".


Example 2:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "aaaa"
Explanation: lcp corresponds to any 4 letter string with a single distinct letter. The lexicographically smallest of them is "aaaa".


Example 3:

Input: lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
Output: ""
Explanation: lcp[3][3] cannot be equal to 3 since word[3,...,3] consists of only a single letter; Thus, no answer exists.


Constraints:

1 <= n == lcp.length == lcp[i].length <= 1000
0 <= lcp[i][j] <= n



################################################################

# TODO

6363. 找出对应 LCP 矩阵的字符串

对任一由 n 个小写英文字母组成的字符串 word ，我们可以定义一个 n x n 的矩阵，并满足：

lcp[i][j] 等于子字符串 word[i,...,n-1] 和 word[j,...,n-1] 之间的最长公共前缀的长度。
给你一个 n x n 的矩阵 lcp 。返回与 lcp 对应的、按字典序最小的字符串 word 。如果不存在这样的字符串，则返回空字符串。

对于长度相同的两个字符串 a 和 b ，如果在 a 和 b 不同的第一个位置，字符串 a 的字母在字母表中出现的顺序先于 b 中的对应字母，则认为字符串 a 按字典序比字符串 b 小。例如，"aabd" 在字典上小于 "aaca" ，因为二者不同的第一位置是第三个字母，而 'b' 先于 'c' 出现。



示例 1：

输入：lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
输出："abab"
解释：lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。


示例 2：

输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
输出："aaaa"
解释：lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。


示例 3：

输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
输出：""
解释：lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。


提示：

1 <= n == lcp.length == lcp[i].length <= 1000
0 <= lcp[i][j] <= n



"""


"""
"""


"""

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/JB73eh/view/Px34pu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

我们对于一个数，考虑最小的一个为 1 的二进制位，设代表 2^k ，其要消去，至少需要进
行一次加上 2^k 或减去 2^k 的操作；而对于只有一个比特位的数，我们的操作数必然为 1。

基于以上观察，我们进行记忆化搜索（也可以通过所有的
2^i 进行 BFS 得到每个数到达 0 的最短路长度，不过总复杂度为 O(MlogM))）。

由于对于所有的状态均进行了记忆化处理，因此，所有用例合在一起的复杂度为O(M).

"""


class Solution:
    @cache
    def minOperations(self, n: int) -> int:
        if n.bit_count() == 1:
            return 1
        x = n - (n & n - 1)
        return min(self.minOperations(n - x), self.minOperations(n + x)) + 1


"""

作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-operations-to-reduce-an-integer-to-0/solution/ji-yi-hua-sou-suo-by-endlesscheng-cm6l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

把 n 看成二进制数，那么更高位的比特 1 是会受到更低位的比特 1 的加减影响的，但是，
最小的比特 1 没有这个约束。

那么考虑优先消除最小的比特 1，设它对应的数字为 lowbit。

消除方法只能是加上 lowbit，或者减去 lowbit。

贪心的策略是：
如果有多个连续 1，那么采用加法是更优的，可以一次消除多个；否则对于单个 1，减法更优。

"""


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 1
        while n & (n - 1):  # 不是 2 的幂次
            lb = n & -n
            if n & (lb << 1):
                n += lb  # 多个连续 1
            else:
                n -= lb  # 单个 1
            ans += 1
        return ans


@cache
def dfs(x: int) -> int:
    if (x & (x - 1)) == 0:  # x 是 2 的幂次
        return 1
    lb = x & -x
    return 1 + min(dfs(x + lb), dfs(x - lb))


class Solution:
    def minOperations(self, n: int) -> int:
        return dfs(n)
