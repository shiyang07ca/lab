"""

# TODO

6216. Minimum Cost to Make Array Equal
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.



Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.


Constraints:

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106

################################################################

6216. 使数组相等的最小开销

给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。

你可以执行下面操作 任意 次：

将 nums 中 任意 元素增加或者减小 1 。
对第 i 个元素执行一次操作的开销是 cost[i] 。

请你返回使 nums 中所有元素 相等 的 最少 总开销。



示例 1：

输入：nums = [1,3,5,2], cost = [2,3,1,14]
输出：8
解释：我们可以执行以下操作使所有元素变为 2 ：
- 增加第 0 个元素 1 次，开销为 2 。
- 减小第 1 个元素 1 次，开销为 3 。
- 减小第 2 个元素 3 次，开销为 1 + 1 + 1 = 3 。
总开销为 2 + 3 + 3 = 8 。
这是最小开销。


示例 2：

输入：nums = [2,2,2,2,2], cost = [4,2,8,1,3]
输出：0
解释：数组中所有元素已经全部相等，不需要执行额外的操作。


提示：

n == nums.length == cost.length
1 <= n <= 105
1 <= nums[i], cost[i] <= 106

"""

"""

"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-cost-to-make-array-equal/solution/by-endlesscheng-i10r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

方法一: 枚举 + 考察变化量

将 nums 和 cost 绑在一起排序。
首先计算使所有元素都等于 nums[0] 的总开销 total，以及所有 cost 的和 sumCost。
然后考虑要使所有元素都等于 nums[1]，total 的变化量是多少：

- 有 cost[0] 这么多的开销要增加 nums[1]−nums[0]；
- 有 sumCost−cost[0] 这么多的开销要减少 nums[1]−nums[0]。

因此 total 减少了 (sumCost−2*cost[0]) * (nums[1]−nums[0])

按照这个公式模拟后续 nums[i]，取所有 total 最小值为答案。

"""


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a = sorted(zip(nums, cost))
        ans = total = sum((x - a[0][0]) * c for x, c in a)
        sum_cost = sum(cost)
        for (x0, c), (x1, _) in pairwise(a):
            sum_cost -= c * 2
            total -= sum_cost * (x1 - x0)
            ans = min(ans, total)
        return ans


"""

方法二：中位数贪心

把 cost[i] 理解成 nums[i] 的出现次数。

根据中位数贪心，把所有数变成中位数是最优的。

详细证明参考 462. 最小操作次数使数组元素相等 II。

"""


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a = sorted(zip(nums, cost))
        s, mid = 0, sum(cost) // 2
        for x, c in a:
            s += c
            if s > mid:  # 把所有数变成 x
                return sum(abs(y - x) * c for y, c in a)
