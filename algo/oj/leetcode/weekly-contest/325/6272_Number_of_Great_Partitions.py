"""
6272. Number of Great Partitions

You are given an array nums consisting of positive integers and an integer k.

Partition the array into two ordered groups such that each element is in exactly one group. A partition is called great if the sum of elements of each group is greater than or equal to k.

Return the number of distinct great partitions. Since the answer may be too large, return it modulo 109 + 7.

Two partitions are considered distinct if some element nums[i] is in different groups in the two partitions.



Example 1:

Input: nums = [1,2,3,4], k = 4
Output: 6
Explanation: The great partitions are: ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) and ([4], [1,2,3]).
Example 2:

Input: nums = [3,3,3], k = 4
Output: 0
Explanation: There are no great partitions for this array.
Example 3:

Input: nums = [6,6], k = 2
Output: 2
Explanation: We can either put nums[0] in the first partition or in the second partition.
The great partitions will be ([6], [6]) and ([6], [6]).


Constraints:

1 <= nums.length, k <= 1000
1 <= nums[i] <= 109

################################################################

TODO
# tag: dp

6272. 好分区的数目

给你一个正整数数组 nums 和一个整数 k 。

分区 的定义是：将数组划分成两个有序的 组 ，并满足每个元素 恰好 存在于 某一个 组中。如果分区中每个组的元素和都大于等于 k ，则认为分区是一个好分区。

返回 不同 的好分区的数目。由于答案可能很大，请返回对 109 + 7 取余 后的结果。

如果在两个分区中，存在某个元素 nums[i] 被分在不同的组中，则认为这两个分区不同。



示例 1：

输入：nums = [1,2,3,4], k = 4
输出：6
解释：好分区的情况是 ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) 和 ([4], [1,2,3]) 。


示例 2：

输入：nums = [3,3,3], k = 4
输出：0
解释：数组中不存在好分区。


示例 3：

输入：nums = [6,6], k = 2
输出：2
解释：可以将 nums[0] 放入第一个分区或第二个分区中。
好分区的情况是 ([6], [6]) 和 ([6], [6]) 。


提示：

1 <= nums.length, k <= 1000
1 <= nums[i] <= 109


"""

"""
"""

"""
作者：endlesscheng
链接：https://leetcode.cn/problems/number-of-great-partitions/solution/ni-xiang-si-wei-01-bei-bao-fang-an-shu-p-v47x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


首先，如果 nums 的所有元素之和都小于 2k，则不存在好分区。

然后考虑计算坏分区的数目，即第一个组或第二个组的元素和小于 k 的方案数。根据对称
性，我们只需要计算第一个组的元素和小于 k 的方案数，然后乘 2 即可。

因此原问题转换成从 nums 中选择若干元素，使得元素和小于 k 的方案数，这可以用 01
背包求解。

定义 f[i][j] 表示从前 i 个数中选择若干元素，和为 j 的方案数。


分类讨论：

- 不选第 i 个数：f[i][j] = f[i-1][j]
- 选第 i 个数：f[i][j] = f[i−1][j−nums[i]]

因此 f[i][j] = f[i-1][j] + f[i−1][j−nums[i]]。

初始值 f[0][0]=1。

坏分区的数目 bad=(f[n][0]+f[n][1]+⋯+f[n][k−1])⋅2。

答案为所有分区的数目减去坏分区的数目，即 2^n-bad, 这里 n 为 nums 的长度。

代码实现时，可以用倒序循环的技巧来压缩空间。

"""


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < k * 2:
            return 0
        MOD = 10**9 + 7
        f = [0] * k
        f[0] = 1
        for x in nums:
            for j in range(k - 1, x - 1, -1):
                f[j] = (f[j] + f[j - x]) % MOD
        return (pow(2, len(nums), MOD) - sum(f) * 2) % MOD


"""
作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/RmydJj/view/cYCjYk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


首先，在总数值小于 k 的情况下不可能满足要求。
接下来，好的分区相对更难处理，我们计算所有不好的分区，不好的分区只有两种情况，一
种是第一组小于 k，一种是第二组小于 k，这我们一起处理，再以总数量减去这两者的方案
数（其实是一致的这两者，且不会有重合）即可得到答案。

因此问题即为在数组中取任意个数使得其和小于 k 的方案数，这是经典的背包问题。

"""

mod = 10**9 + 7


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums) < 2 * k:
            return 0
        n = len(nums)
        tot_method = pow(2, n, mod)

        @cache
        def getRes(idx, space):
            if idx == n:
                return 1
            res = getRes(idx + 1, space)
            if nums[idx] < space:
                res += getRes(idx + 1, space - nums[idx])
            return res % mod

        ans = (tot_method - getRes(0, k) * 2) % mod
        getRes.cache_clear()
        return ans
