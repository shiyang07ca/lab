# Created by shiyang07ca at 2023/09/24 10:33
# leetgo: dev
# https://leetcode.cn/problems/beautiful-towers-ii/
# https://leetcode.cn/contest/weekly-contest-364/problems/beautiful-towers-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


# 链接：https://leetcode.cn/problems/beautiful-towers-ii/

"""
要点
1. 相同的数，需要保留最靠在的那一个（的下标）
2. 用单调栈维护需要保留的数

3. 如何维护元素和


"""
class Solution:
    def maximumSumOfHeights(self, a: List[int]) -> int:
        n = len(a)
        suf = [0] * (n + 1)
        st = [n]  # 哨兵
        s = 0
        for i in range(n - 1, -1, -1):
            x = a[i]
            while len(st) > 1 and x <= a[st[-1]]:
                j = st.pop()
                s -= a[j] * (st[-1] - j)  # 撤销之前加到 s 中的
            s += x * (st[-1] - i)  # 从 i 到 st[-1]-1 都是 x
            suf[i] = s
            st.append(i)

        ans = s
        st = [-1]  # 哨兵
        pre = 0
        for i, x in enumerate(a):
            while len(st) > 1 and x <= a[st[-1]]:
                j = st.pop()
                pre -= a[j] * (j - st[-1])  # 撤销之前加到 pre 中的
            pre += x * (i - st[-1])  # 从 st[-1]+1 到 i 都是 x
            ans = max(ans, pre + suf[i + 1])
            st.append(i)
        return ans


# @lc code=end

if __name__ == "__main__":
    maxHeights: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSumOfHeights(maxHeights)

    print("\noutput:", serialize(ans))
