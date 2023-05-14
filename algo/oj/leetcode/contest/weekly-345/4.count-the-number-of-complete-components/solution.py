# Created by shiyang07ca at 2023/05/14 10:30
# https://leetcode.cn/problems/count-the-number-of-complete-components/
# https://leetcode.cn/contest/weekly-contest-345/problems/count-the-number-of-complete-components/

"""
6432. 统计完全连通分量的数量 (Medium)
给你一个整数 `n` 。现有一个包含 `n` 个顶点的 **无向** 图，顶
点按从 `0` 到 `n - 1` 编号。给你一个二维整数数组 `edges` 其
中 `edges[i] = [aᵢ, bᵢ]` 表示顶点 `aᵢ` 和 `bᵢ` 之间存在一条
**无向** 边。

返回图中 **完全连通分量** 的数量。

如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一
个顶点与子图外部的顶点共享边，则称其为 **连通分量** 。

如果连通分量中每对节点之间都存在一条边，则称其为 **完全连通
分量** 。

**示例 1：**

**![](https://assets.leetcode.com/uploads/2023/04/11/screens
hot-from-2023-04-11-23-31-23.png)**

```
输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
输出：3
解释：如上图所示，可以看到此图所有分量都是完全连通分量。

```

**示例 2：**

**![](https://assets.leetcode.com/uploads/2023/04/11/screens
hot-from-2023-04-11-23-32-00.png)**

```
输入：n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
输出：1
解释：包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点
之间都存在一条边。
包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5
之间不存在边。
因此，在图中完全连接分量的数量是 1 。

```

**提示：**

- `1 <= n <= 50`
- `0 <= edges.length <= n * (n - 1) / 2`
- `edges[i].length == 2`
- `0 <= aᵢ, bᵢ <= n - 1`
- `aᵢ != bᵢ`
- 不存在重复的边

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO

"""
作者：灵茶山艾府
链接：https://leetcode.cn/problems/count-the-number-of-complete-components/solutions/2269255/dfs-qiu-mei-ge-lian-tong-kuai-de-dian-sh-opg4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        vis = [False] * n

        def dfs(x: int) -> None:
            vis[x] = True
            nonlocal v, e
            v += 1
            e += len(g[x])
            for y in g[x]:
                if not vis[y]:
                    dfs(y)

        ans = 0
        for i, b in enumerate(vis):
            if not b:
                v = e = 0
                dfs(i)
                ans += e == v * (v - 1)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().countCompleteComponents(n, edges)
    print("output:", serialize(ans))
