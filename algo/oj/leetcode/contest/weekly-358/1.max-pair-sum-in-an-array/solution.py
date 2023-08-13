# Created by shiyang07ca at 2023/08/13 10:32
# leetgo: dev
# https://leetcode.cn/problems/max-pair-sum-in-an-array/
# https://leetcode.cn/contest/weekly-contest-358/problems/max-pair-sum-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/circle/discuss/9wQ08W/view/4drty4/
    def maxSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for x in nums:
            d[max(str(x))].append(x)
        ans = -1
        for v in d:
            if len(d[v]) >= 2:
                # nlargest 复杂度是 n log k 的，这里 k = 2，因此可以认为是常数
                ans = max(ans, sum(nlargest(2, d[v])))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSum(nums)

    print("\noutput:", serialize(ans))
