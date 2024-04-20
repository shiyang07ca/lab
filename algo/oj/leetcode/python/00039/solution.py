# Created by shiyang07ca at 2024/04/20 13:54
# leetgo: dev
# https://leetcode.cn/problems/combination-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def dfs(i, target):
            if target == 0:  # 找到答案
                ans.append(path[:])
                return

            if i == len(candidates) or target < candidates[i]:
                return

            path.append(candidates[i])  # 选
            dfs(i, target - candidates[i])
            path.pop()  # 恢复现场

            dfs(i + 1, target)  # 不选

        dfs(0, target)
        return ans


# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
