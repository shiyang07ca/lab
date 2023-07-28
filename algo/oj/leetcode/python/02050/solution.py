# Created by shiyang07ca at 2023/07/28 12:44
# leetgo: dev
# https://leetcode.cn/problems/parallel-courses-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

# template
# TODO


# 链接：https://leetcode.cn/problems/parallel-courses-iii/solutions/2362108/python3javacgotypescript-yi-ti-yi-jie-tu-4nbv/
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = defaultdict(list)
        indeg = [0] * n
        for a, b in relations:
            g[a - 1].append(b - 1)
            indeg[b - 1] += 1
        q = deque()
        f = [0] * n
        ans = 0
        for i, (v, t) in enumerate(zip(indeg, time)):
            if v == 0:
                q.append(i)
                f[i] = t
                ans = max(ans, t)
        while q:
            i = q.popleft()
            for j in g[i]:
                f[j] = max(f[j], f[i] + time[j])
                ans = max(ans, f[j])
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTime(n, relations, time)

    print("\noutput:", serialize(ans))
