"""
2547. Minimum Cost to Split an Array

You are given an integer array nums and an integer k.

Split the array into some number of non-empty subarrays. The cost of a split is the sum of the importance value of each subarray in the split.

Let trimmed(subarray) be the version of the subarray where all numbers which appear only once are removed.

For example, trimmed([3,1,2,4,3,4]) = [3,4,3,4].
The importance value of a subarray is k + trimmed(subarray).length.

For example, if a subarray is [1,2,3,3,3,4,4], then trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4].The importance value of this subarray will be k + 5.
Return the minimum possible cost of a split of nums.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,2,1,2,1,3,3], k = 2
Output: 8
Explanation: We split nums to have two subarrays: [1,2], [1,2,1,3,3].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1,3,3] is 2 + (2 + 2) = 6.
The cost of the split is 2 + 6 = 8. It can be shown that this is the minimum possible cost among all the possible splits.
Example 2:

Input: nums = [1,2,1,2,1], k = 2
Output: 6
Explanation: We split nums to have two subarrays: [1,2], [1,2,1].
The importance value of [1,2] is 2 + (0) = 2.
The importance value of [1,2,1] is 2 + (2) = 4.
The cost of the split is 2 + 4 = 6. It can be shown that this is the minimum possible cost among all the possible splits.
Example 3:

Input: nums = [1,2,1,2,1], k = 5
Output: 10
Explanation: We split nums to have one subarray: [1,2,1,2,1].
The importance value of [1,2,1,2,1] is 5 + (3 + 2) = 10.
The cost of the split is 10. It can be shown that this is the minimum possible cost among all the possible splits.


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
1 <= k <= 109

################################################################

# TODO
# tag: dp

2547. 拆分数组的最小代价

给你一个整数数组 nums 和一个整数 k 。

将数组拆分成一些非空子数组。拆分的 代价 是每个子数组中的 重要性 之和。

令 trimmed(subarray) 作为子数组的一个特征，其中所有仅出现一次的数字将会被移除。

例如，trimmed([3,1,2,4,3,4]) = [3,4,3,4] 。
子数组的 重要性 定义为 k + trimmed(subarray).length 。

例如，如果一个子数组是 [1,2,3,3,3,4,4] ，trimmed([1,2,3,3,3,4,4]) = [3,3,3,4,4] 。这个子数组的重要性就是 k + 5 。
找出并返回拆分 nums 的所有可行方案中的最小代价。

子数组 是数组的一个连续 非空 元素序列。



示例 1：

输入：nums = [1,2,1,2,1,3,3], k = 2
输出：8
解释：将 nums 拆分成两个子数组：[1,2], [1,2,1,3,3]
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1,3,3] 的重要性是 2 + (2 + 2) = 6 。
拆分的代价是 2 + 6 = 8 ，可以证明这是所有可行的拆分方案中的最小代价。


示例 2：

输入：nums = [1,2,1,2,1], k = 2
输出：6
解释：将 nums 拆分成两个子数组：[1,2], [1,2,1] 。
[1,2] 的重要性是 2 + (0) = 2 。
[1,2,1] 的重要性是 2 + (2) = 4 。
拆分的代价是 2 + 4 = 6 ，可以证明这是所有可行的拆分方案中的最小代价。


示例 3：

输入：nums = [1,2,1,2,1], k = 5
输出：10
解释：将 nums 拆分成一个子数组：[1,2,1,2,1].
[1,2,1,2,1] 的重要性是 5 + (3 + 2) = 10 。
拆分的代价是 10 ，可以证明这是所有可行的拆分方案中的最小代价。


提示：

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
1 <= k <= 109

"""


"""
作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/Kclgr5/view/0iye2F/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

注意到拆分完一个数组后，剩下的子数组会对应一个形式相同的子问题，因此考虑使用动态
规划。

而我们也类似的构造动态规划，认为从 idx 开始的子数组的最小代价为 dp[idx]，接下来
只需要求得 dp[0] 即可。

我们考虑状态转移：对于 0≤i<j≤n 如何从 j 转移到 i. 这里我们只需要看中间对应的子数
组trimmed 后的结果，而对于这个，我们无需每次重新计算，可以固定一个 i 往后走时对
频率计数计算代价，也可以固定 j 往前走时统计频率。这样我们就成功把复杂度控制在了
O(n^2)

"""

# 写法一：递归
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)

        @cache
        def getRes(idx):
            if idx == n:
                return 0
            tmp = defaultdict(int)
            cnt = 0
            ans = inf
            for i in range(idx, n):
                if tmp[nums[i]] == 1:
                    cnt += 2
                elif tmp[nums[i]] > 1:
                    cnt += 1
                tmp[nums[i]] += 1
                ans = min(ans, getRes(i + 1) + cnt + k)
            return ans

        res = getRes(0)
        getRes.cache_clear()
        return res


# 写法二：数组
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [inf] * (n + 1)
        dp[n] = 0
        for i in range(n, -1, -1):
            cnt = defaultdict(int)
            cost = k
            for j in range(i - 1, -1, -1):
                if cnt[nums[j]] == 1:
                    cost += 2
                elif cnt[nums[j]] > 1:
                    cost += 1
                cnt[nums[j]] += 1
                dp[j] = min(dp[j], dp[i] + cost)
        return dp[0]


# TODO
# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/minimum-cost-to-split-an-array/solution/by-endlesscheng-05s0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # Lazy 线段树模板（区间加，查询区间最小）
        n = len(nums)
        mn = [0] * (4 * n)
        todo = [0] * (4 * n)

        def do(o: int, v: int) -> None:
            mn[o] += v
            todo[o] += v

        def spread(o: int) -> None:
            v = todo[o]
            if v:
                do(o * 2, v)
                do(o * 2 + 1, v)
                todo[o] = 0

        # 区间 [L,R] 内的数都加上 v   o,l,r=1,1,n
        def update(o: int, l: int, r: int, L: int, R: int, v: int) -> None:
            if L <= l and r <= R:
                do(o, v)
                return
            spread(o)
            m = (l + r) // 2
            if m >= L:
                update(o * 2, l, m, L, R, v)
            if m < R:
                update(o * 2 + 1, m + 1, r, L, R, v)
            mn[o] = min(mn[o * 2], mn[o * 2 + 1])

        # 查询区间 [L,R] 的最小值   o,l,r=1,1,n
        def query(o: int, l: int, r: int, L: int, R: int) -> int:
            if L <= l and r <= R:
                return mn[o]
            spread(o)
            m = (l + r) // 2
            if m >= R:
                return query(o * 2, l, m, L, R)
            if m < L:
                return query(o * 2 + 1, m + 1, r, L, R)
            return min(query(o * 2, l, m, L, R), query(o * 2 + 1, m + 1, r, L, R))

        ans = 0
        last = [0] * n
        last2 = [0] * n
        for i, x in enumerate(nums, 1):
            update(1, 1, n, i, i, ans)  # 相当于设置 f[i+1] 的值
            update(1, 1, n, last[x] + 1, i, -1)
            if last[x]:
                update(1, 1, n, last2[x] + 1, last[x], 1)
            ans = k + query(1, 1, n, 1, i)
            last2[x] = last[x]
            last[x] = i
        return ans + n
