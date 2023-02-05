"""

6346. House Robber IV

There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

Return the minimum capability of the robber out of all the possible ways to steal at least k houses.



Example 1:

Input: nums = [2,3,5,9], k = 2
Output: 5
Explanation:
There are three ways to rob at least 2 houses:
- Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
- Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
- Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
Therefore, we return min(5, 9, 9) = 5.
Example 2:

Input: nums = [2,7,9,3,1], k = 2
Output: 2
Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2

################################################################


# TODO
# tag: binary search, dp

6346. 打家劫舍 IV

沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。

由于相邻的房屋装有相互连通的防盗系统，所以小偷 不会窃取相邻的房屋 。

小偷的 窃取能力 定义为他在窃取过程中能从单间房屋中窃取的 最大金额 。

给你一个整数数组 nums 表示每间房屋存放的现金金额。形式上，从左起第 i 间房屋中放有 nums[i] 美元。

另给你一个整数数组 k ，表示窃贼将会窃取的 最少 房屋数。小偷总能窃取至少 k 间房屋。

返回小偷的 最小 窃取能力。



示例 1：

输入：nums = [2,3,5,9], k = 2
输出：5
解释：
小偷窃取至少 2 间房屋，共有 3 种方式：
- 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
- 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
- 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
因此，返回 min(5, 9, 9) = 5 。


示例 2：

输入：nums = [2,7,9,3,1], k = 2
输出：2
解释：共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= (nums.length + 1)/2


"""


"""
作者：endlesscheng
链接：https://leetcode.cn/problems/house-robber-iv/solution/er-fen-da-an-dp-by-endlesscheng-m558/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


设二分的最大金额为 mx，定义 f[i] 表示在前 i 个房屋中窃取金额不超过 mx 的房屋最大个数

分类讨论：
  * 不选第 i 个房屋：f[i] = f[i-1]
  * 选第 i 个房屋，前提是金额不超过 mx：f[i] = f[i-2] + 1
两者取最大值，即
       f[i] = max(f[i−1], f[i−2]+1)

代码实现时，可以用两个变量滚动计算。

"""


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mx):
            f0 = f1 = 0
            for n in nums:
                if n > mx:
                    f0 = f1
                else:
                    f0, f1 = f1, max(f1, f0 + 1)
            return f1

        l, r = 0, max(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l


"""
作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/2Gdn7F/view/43FuHN/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



不难发现这里，窃贼的窃取能力增加，能窃取的房屋数量单调不减。

因此求一个窃取能力的下界可以考虑使用二分解决。

我们接下来只需要查看对于某一个窃取能力最多能窃取多少房屋。这个我们可以通过动态规
划得到，记录两个变量 dp0, dp1 分别代表这个位置盗窃和不盗窃情况下窃取的房屋数量，
再根据当前位置房屋情况进行转移（详情看代码注释）。

"""


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r) // 2
            dp0, dp1 = 0, 0
            for num in nums:
                # 有能力窃取时：
                # 当前位置不窃取：从前一房屋的两状态中取最大值
                # 当前位置窃取：前一房屋只能不窃取
                if num <= m:
                    dp0, dp1 = max(dp0, dp1), dp0 + 1
                # 没有能力窃取时：
                # 当前位置不窃取：从前一房屋的两状态中取最大值
                # 当前位置无法窃取，方法数为 0
                else:
                    dp0, dp1 = max(dp0, dp1), 0
            if max(dp0, dp1) >= k:
                r = m - 1
            else:
                l = m + 1
        return l
