# Created by shiyang07ca at 2023/09/24 10:33
# leetgo: dev
# https://leetcode.cn/problems/count-valid-paths-in-a-tree/
# https://leetcode.cn/contest/weekly-contest-364/problems/count-valid-paths-in-a-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countPaths(n, edges)

    print("\noutput:", serialize(ans))
