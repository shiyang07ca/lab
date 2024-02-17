# Created by shiyang07ca at 2023/07/29 19:41
# leetgo: dev
# https://leetcode.cn/problems/longest-subsequence-with-limited-sum/
# https://leetcode.cn/contest/weekly-contest-308/problems/longest-subsequence-with-limited-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().answerQueries(nums, queries)

    print("\noutput:", serialize(ans))
