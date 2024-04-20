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
        N = len(candidates)
        candidates.sort()

        def dfs(i, target, cur):
            if i == N or candidates[i] > target:
                return

            if candidates[i] == target:
                cur.append(candidates[i])
                ans.append(cur)
            else:
                cur.append(candidates[i])
                dfs(i, target - candidates[i], cur[:])
                cur.pop()
                dfs(i + 1, target, cur[:])

        dfs(0, target, [])
        return ans


# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
