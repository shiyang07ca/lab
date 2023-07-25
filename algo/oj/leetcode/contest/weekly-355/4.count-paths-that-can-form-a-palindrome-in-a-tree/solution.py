# Created by shiyang07ca at 2023/07/25 22:58
# leetgo: dev
# https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/
# https://leetcode.cn/contest/weekly-contest-355/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin


# TODO

# 链接：https://leetcode.cn/problems/count-paths-that-can-form-a-palindrome-in-a-tree/solutions/2355288/yong-wei-yun-suan-chu-li-by-endlesscheng-n9ws/

"""
* 回文串等价于至多一个字母出现奇数次，其余字母出现偶数次


* 用一个长为 26 的二进制数来压缩存储每个字母的奇偶性，一条边可以看成是 1 << (s[i]-'a')
  那么路径所对应的二进制数，就是路径上所有边的异或和
  只有 27 个二进制数符合要求：
  - 0，表示每个字母都出现偶数次
  - 2^0, 2^1, ..., 2^25，表示第 i 个字母出现奇数次，其余字母出现偶数次


* 设 v 和 w 的最近公共祖先为 lca，设从根到 i 的路径异或和为 XORi
  v 到 w 的路径可以看成是 v-lca-w，其中 lca 到 v 的路径异或和，等于根到 v 的异或和，再异或上根到
  lca 的异或和。lca 到 w 的路径异或和也同理。

  所以 v-lca-w 的异或和为：
                   （XORv ⊕ XORlca）⊕ (XORw ⊕ XORlca)

  XORlca 异或了两次，抵消掉，所以上式为：
                    XORv ⊕ XORw

  把所有的 XORi 求出来，就变成判断这 n-1 个数当中：

  * 两数异或和是否为 0？这意味着路径上的每个字母都会出现偶数次。

  * 两数异或和是否为 2 的幂？这意味着路径上恰好有个字母出现奇数次，其余字母出现偶数次。

  * 特殊情况：XORi = 0 或者 XORi 为 2 的幂，表示从根到 i 的路径符合要求，我们可
    以异或上一条空路径对应的异或值，即 0，就转换成了上面两数异或和的情况。

  这可以用类似两数之和的思路解决，用哈希表记录 XORi 的个数，设当前算出的异或和为
  x，去哈希表中找 x 的出现次数以及 x ⊕ 2^k 的出现次数


"""


class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ans = 0
        cnt = Counter([0])  # 一条「空路径」

        def dfs(v: int, xor: int) -> None:
            nonlocal ans
            for w in g[v]:
                bit = 1 << (ord(s[w]) - ord("a"))
                x = xor ^ bit
                ans += cnt[x] + sum(cnt[x ^ (1 << i)] for i in range(26))
                cnt[x] += 1
                dfs(w, x)

        dfs(0, 0)
        return ans

    # 链接：https://leetcode.cn/circle/discuss/1AqXeK/view/L7qGfY/
    def countPalindromePaths2(self, parent: List[int], s: str) -> int:
        n = len(parent)

        @cache
        def getRes(idx):
            if idx == 0:
                return 0
            return getRes(parent[idx]) ^ (1 << (ord(s[idx]) - ord("a")))

        vals = [getRes(i) for i in range(n)]
        cnt = Counter()
        ans = 0
        for x in vals:
            ans += cnt[x]
            for i in range(26):
                ans += cnt[x ^ (1 << i)]
            cnt[x] += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    parent: List[int] = deserialize("List[int]", read_line())
    s: str = deserialize("str", read_line())
    ans = Solution().countPalindromePaths(parent, s)

    print("\noutput:", serialize(ans))
