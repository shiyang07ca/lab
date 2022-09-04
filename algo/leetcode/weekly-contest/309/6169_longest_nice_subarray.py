"""

# TODO

6169. 最长优雅子数组


给你一个由 正 整数组成的数组 nums 。

如果 nums 的子数组中位于 不同 位置的每对元素按位 与（AND）运算的结果等于 0 ，则称该子数组为 优雅 子数组。

返回 最长 的优雅子数组的长度。

子数组 是数组中的一个 连续 部分。

注意：长度为 1 的子数组始终视作优雅子数组。



示例 1：

输入：nums = [1,3,8,48,10]
输出：3
解释：最长的优雅子数组是 [3,8,48] 。子数组满足题目条件：
- 3 AND 8 = 0
- 3 AND 48 = 0
- 8 AND 48 = 0
可以证明不存在更长的优雅子数组，所以返回 3 。



示例 2：

输入：nums = [3,1,5,11,13]
输出：1
解释：最长的优雅子数组长度为 1 ，任何长度为 1 的子数组都满足题目条件。


提示：

1 <= nums.length <= 105
1 <= nums[i] <= 109

"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        ans = 1
        # dp[i] 表示以 num[i] 为结尾的数组中，优雅数组的最长长度以及他们的和
        dp = [(1, nums[0])]

        for i in range(1, len(nums)):
            num = nums[i]
            pre_len, pre_sum = dp[i - 1]

            if pre_sum & num == 0:
                dp.append((pre_len + 1, pre_sum + num))
                ans = max(ans, pre_len + 1)
            else:
                # 回退校验符合条件的的优雅数组，填充到 dp 数组中
                if nums[i - 1] & num == 0:
                    count = 2
                    total = num + nums[i - 1]
                    for n in nums[i - 2 : 0 : -1]:
                        if n & total == 0:
                            count += 1
                            total += n
                        else:
                            break
                    dp.append((count, total))

                else:
                    dp.append((1, num))

        return ans


################################################################


# 其他解法
# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/longest-nice-subarray/solution/bao-li-mei-ju-pythonjavacgo-by-endlessch-z6t6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 暴力枚举

# 复杂度分析
# 时间复杂度：O(nlogmax(nums))，其中 n 为 nums 的长度。
# 空间复杂度：O(1)O(1)，仅用到若干变量。


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        for i, or_ in enumerate(nums):
            j = i - 1
            while j >= 0 and (or_ & nums[j]) == 0:
                or_ |= nums[j]
                j -= 1
            ans = max(ans, i - j)
        return ans


"""

可以用双指针优化上述过程，如果当前 or 与 nums[right] 按位与结果不为 0，则从 or 中
去掉 nums[left]，并将 left 右移

"""


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = left = or_ = 0
        for right, x in enumerate(nums):
            while or_ & x:
                or_ ^= nums[left]
                left += 1
            or_ |= x
            ans = max(ans, right - left + 1)
        return ans
