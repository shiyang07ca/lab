"""

6230. 长度为 K 子数组中的最大和
给你一个整数数组 nums 和一个整数 k 。请你从 nums 中满足下述条件的全部子数组中找出最大子数组和：

子数组的长度是 k，且
子数组中的所有元素 各不相同 。
返回满足题面要求的最大子数组和。如果不存在子数组满足这些条件，返回 0 。

子数组 是数组中一段连续非空的元素序列。



示例 1：

输入：nums = [1,5,4,2,9,9,9], k = 3
输出：15
解释：nums 中长度为 3 的子数组是：
- [1,5,4] 满足全部条件，和为 10 。
- [5,4,2] 满足全部条件，和为 11 。
- [4,2,9] 满足全部条件，和为 15 。
- [2,9,9] 不满足全部条件，因为元素 9 出现重复。
- [9,9,9] 不满足全部条件，因为元素 9 出现重复。
因为 15 是满足全部条件的所有子数组中的最大子数组和，所以返回 15 。


示例 2：

输入：nums = [4,4,4], k = 3
输出：0
解释：nums 中长度为 3 的子数组是：
- [4,4,4] 不满足全部条件，因为元素 4 出现重复。
因为不存在满足全部条件的子数组，所以返回 0 。


提示：

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105

"""

"""

一个大小为 kk 的滑动窗口。

用一个哈希表 cnt 维护窗口内的元素个数，以及窗口内的元素和 sum，如果 cnt 的大小等于 k，
说明找到了 k 个互不相同的元素，用此时的 sum 更新答案的最大值。

作者：endlesscheng
链接：https://leetcode.cn/problems/maximum-sum-of-distinct-subarrays-with-length-k/solution/hua-dong-chuang-kou-by-endlesscheng-m0gm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter(nums[: k - 1])
        s = sum(nums[: k - 1])
        for in_, out in zip(nums[k - 1 :], nums):
            cnt[in_] += 1  # 移入元素
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1  # 移出元素
            if cnt[out] == 0:
                del cnt[out]  # 重要：及时移除个数为 0 的数据
            s -= out
        return ans
