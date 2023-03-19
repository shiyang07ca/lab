"""

6352. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.



Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].


Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].


Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000

################################################################

https://leetcode.cn/contest/weekly-contest-337/problems/the-number-of-beautiful-subsets/

# TODO

6352. 美丽子集的数目

给你一个由正整数组成的数组 nums 和一个 正 整数 k 。

如果 nums 的子集中，任意两个整数的绝对差均不等于 k ，则认为该子数组是一个 美丽 子集。

返回数组 nums 中 非空 且 美丽 的子集数目。

nums 的子集定义为：可以经由 nums 删除某些元素（也可能不删除）得到的一个数组。只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。



示例 1：

输入：nums = [2,4,6], k = 2
输出：4
解释：数组 nums 中的美丽子集有：[2], [4], [6], [2, 6] 。
可以证明数组 [2,4,6] 中只存在 4 个美丽子集。


示例 2：

输入：nums = [1], k = 1
输出：1
解释：数组 nums 中的美丽数组有：[1] 。
可以证明数组 [1] 中只存在 1 个美丽子集。


提示：

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
"""

"""

LC78. 子集 https://leetcode.cn/problems/subsets/
LC784. 字母大小写全排列 https://leetcode.cn/problems/letter-case-permutation/
LC1601. 最多可达成的换楼请求数目 https://leetcode.cn/problems/maximum-number-of-achievable-transfer-requests/
LC2397. 被列覆盖的最多行数 https://leetcode.cn/problems/maximum-rows-covered-by-columns/

"""

# 写法一：选或不选


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = [0] * (max(nums) + k * 2)  # 用数组实现比哈希表更快

        def dfs(i: int) -> None:
            if i == len(nums):
                nonlocal ans
                ans += 1
                return
            dfs(i + 1)  # 不选
            x = nums[i]
            if cnt[x - k] == 0 and cnt[x + k] == 0:
                cnt[x] += 1  # 选
                dfs(i + 1)
                cnt[x] -= 1  # 恢复现场

        dfs(0)
        return ans


# 写法二：枚举选哪个


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        ans = -1  # 去掉空集
        cnt = [0] * (max(nums) + k * 2)  # 用数组实现比哈希表更快

        def dfs(i: int) -> None:  # 从 i 开始选
            nonlocal ans
            ans += 1
            if i == len(nums):
                return
            for j in range(i, len(nums)):  # 枚举选哪个
                x = nums[j]
                if cnt[x - k] == 0 and cnt[x + k] == 0:
                    cnt[x] += 1  # 选
                    dfs(j + 1)
                    cnt[x] -= 1  # 恢复现场

        dfs(0)
        return ans
