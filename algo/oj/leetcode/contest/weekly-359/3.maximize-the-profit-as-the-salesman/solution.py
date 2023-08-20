# Created by shiyang07ca at 2023/08/20 13:23
# leetgo: dev
# https://leetcode.cn/problems/maximize-the-profit-as-the-salesman/
# https://leetcode.cn/contest/weekly-contest-359/problems/maximize-the-profit-as-the-salesman/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


"""
https://leetcode.cn/problems/maximize-the-profit-as-the-salesman/solutions/2396402/xian-xing-dpfu-xiang-si-ti-mu-pythonjava-wmh7/


定义 f[i+1] 表示销售编号不超过 i 的最大金币数

考虑编号为 i 的房屋卖或不卖：

* 不卖，有 f[i+1] = f[i]
* 卖，那么遍历所有 end_j = i 的购买请求，有 f[i+1] = max(f[start_j] + gold_j)。
  为了方便遍历，可以先把所有 end 相同的数据用哈希表归类
* 两种情况取最大值

初始值 f[0] = 0

最终答案为 f[n]



相似题目

LC2008. 出租车的最大盈利
https://leetcode.cn/problems/maximum-earnings-from-taxi/


LC1235. 规划兼职工作
https://leetcode.cn/problems/maximum-profit-in-job-scheduling/


LC1751. 最多可以参加的会议数目 II
https://leetcode.cn/problems/maximum-number-of-events-that-can-be-attended-ii/


LC2054. 两个最好的不重叠活动
https://leetcode.cn/problems/two-best-non-overlapping-events/

"""


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        groups = [[] for _ in range(n)]
        for start, end, gold in offers:
            groups[end].append((start, gold))
        f = [0] * (n + 1)
        for end, g in enumerate(groups):
            f[end + 1] = f[end]
            for start, gold in g:
                f[end + 1] = max(f[end + 1], f[start] + gold)
        return f[n]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    offers: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximizeTheProfit(n, offers)

    print("\noutput:", serialize(ans))
