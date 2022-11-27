"""

6248. Count Subarrays With Median K

You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

Return the number of non-empty subarrays in nums that have a median equal to k.

Note:

The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
A subarray is a contiguous part of an array.


Example 1:

Input: nums = [3,2,1,4,5], k = 4
Output: 3
Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].
Example 2:

Input: nums = [2,3,1], k = 3
Output: 1
Explanation: [3] is the only subarray that has a median equal to 3.


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i], k <= n
The integers in nums are distinct.

"""


"""

6248. 统计中位数为 K 的子数组

给你一个长度为 n 的数组 nums ，该数组由从 1 到 n 的 不同 整数组成。另给你一个正
整数 k 。

统计并返回 num 中的 中位数 等于 k 的非空子数组的数目。


注意：

数组的中位数是按 递增 顺序排列后位于 中间 的那个元素，如果数组长度为偶数，则中位
数是位于中间靠 左 的那个元素。

例如，[2,3,1,4] 的中位数是 2 ，[8,4,3,5,1] 的中位数是 4 。
子数组是数组中的一个连续部分。


示例 1：

输入：nums = [3,2,1,4,5], k = 4
输出：3
解释：中位数等于 4 的子数组有：[4]、[4,5] 和 [1,4,5] 。


示例 2：

输入：nums = [2,3,1], k = 3
输出：1
解释：[3] 是唯一一个中位数等于 3 的子数组。


提示：

n == nums.length
1 <= n <= 10^5
1 <= nums[i], k <= n
nums 中的整数互不相同

"""

"""
LC 剑指 Offer II 010. 和为 k 的子数组https://leetcode.cn/problems/QTMn0o/

https://algo.itcharge.cn/Solutions/Offer-II/QTMn0o/

pre_sum[i] 的定义是前 i 个元素和，则 pre_sum[i] 可以由 pre_sum[i - 1] 递推而来，
即：pre_sum[i] = pre_sum[i - 1] + sum[i]。 [j..i] 子数组和为 k 可以转换为：
pre_sum[i] - pre_sum[j - 1] == k。


综合一下，可得：pre_sum[j - 1] == pre_sum[i] - k 。

所以，当我们考虑以 i 结尾和为 k 的连续子数组个数时，只需要统计有多少个前缀和为
pre_sum[i] - k （即 pre_sum[j - 1]）的个数即可。具体做法如下：


* 使用 pre_sum 变量记录前缀和（代表 pre_sum[i]）。
* 使用哈希表 pre_dic 记录 pre_sum[i] 出现的次数。键值对为 pre_sum[i] : pre_sum_count。
* 从左到右遍历数组，计算当前前缀和 pre_sum。
* 如果 pre_sum - k 在哈希表中，则答案个数累加上 pre_dic[pre_sum - k]。
* 如果 pre_sum 在哈希表中，则前缀和个数累加 1，即 pre_dic[pre_sum] += 1。
* 最后输出答案个数。

"""


class Solution:
    def countSubarrays(self, nums: List[int], t: int) -> int:
        # 求和为 k 的子数组数目
        def subarraySum(nums, k):
            pre_dic = {0: 1}
            pre_sum = 0
            count = 0
            for num in nums:
                pre_sum += num
                if pre_sum - k in pre_dic:
                    count += pre_dic[pre_sum - k]
                if pre_sum in pre_dic:
                    pre_dic[pre_sum] += 1
                else:
                    pre_dic[pre_sum] = 1
            return count

        a = []
        N = len(nums)
        for n in nums:
            if n > t:
                a.append(1)
            elif n < t:
                a.append(-1)
            else:
                a.append(N)
        a1 = subarraySum(a, N)
        a2 = subarraySum(a, N + 1)
        #         print(a1, a2)

        return a1 + a2


"""

作者：endlesscheng
链接：https://leetcode.cn/problems/count-subarrays-with-median-k/solution/deng-jie-zhuan-huan-pythonjavacgo-by-end-5w11/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

展开成一个数学式子
中位数 =>
     奇数长度: 小于 = 大于
     偶数长度: 小于 + 1 = 大于

+左侧小于 + 右侧小于 (+ 1) =  +左侧大于 + 右侧大于
+左侧小于 - 左侧大于 (+ 1) =  +右侧大于 - 右侧小于

"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt = defaultdict(int)
        cnt[0] = 1  # i=pos 的时候 c 是 0，直接记到 cnt 中，这样下面不是大于就是小于
        c = 0
        for i in range(pos + 1, len(nums)):
            c += 1 if nums[i] > k else -1
            cnt[c] += 1

        ans = cnt[0] + cnt[1]  # i=pos 的时候 c 是 0，直接加到答案中，这样下面不是大于就是小于
        c = 0
        for i in range(pos - 1, -1, -1):
            c += 1 if nums[i] < k else -1
            ans += cnt[c] + cnt[c + 1]
        return ans
