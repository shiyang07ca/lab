# Created by shiyang07ca at 2023/08/19 23:35
# leetgo: dev
# https://leetcode.cn/problems/sorting-three-groups/
# https://leetcode.cn/contest/biweekly-contest-111/problems/sorting-three-groups/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums) - 1

        @cache
        def dfs(i, x):
            y = nums[i]
            if i == 0:
                return 0 if x == y else 1

            if x == y:
                if x == 1:
                    return dfs(i - 1, 1)
                elif x == 2:
                    return min(dfs(i - 1, 2), dfs(i - 1, 1))
                elif x == 3:
                    return min(dfs(i - 1, 3), dfs(i - 1, 2), dfs(i - 1, 1))
            else:
                if x == 1:
                    return dfs(i - 1, 1) + 1
                elif x == 2:
                    return min(dfs(i - 1, 2) + 1, dfs(i - 1, 1) + 1)
                elif x == 3:
                    return min(dfs(i - 1, 3) + 1, dfs(i - 1, 2) + 1, dfs(i - 1, 1) + 1)

        return min(dfs(n, 1), dfs(n, 2), dfs(n, 3))

    # 链接：https://leetcode.cn/problems/sorting-three-groups/solutions/2396466/liang-chong-fei-bao-li-zuo-fa-liszhuang-38zac/
    # 转换成最多可以保留多少个元素不变。这些保留的元素必须是非递减的
    def minimumOperations2(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_right(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
        return len(nums) - len(g)

    # TODO: 状态机dp


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumOperations(nums)

    print("\noutput:", serialize(ans))
