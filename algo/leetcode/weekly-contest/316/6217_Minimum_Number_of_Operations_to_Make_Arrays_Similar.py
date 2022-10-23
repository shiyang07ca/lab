"""

# TODO

6217. Minimum Number of Operations to Make Arrays Similar
You are given two positive integer arrays nums and target, of the same length.

In one operation, you can choose any two distinct indices i and j where 0 <= i, j < nums.length and:

set nums[i] = nums[i] + 2 and
set nums[j] = nums[j] - 2.
Two arrays are considered to be similar if the frequency of each element is the same.

Return the minimum number of operations required to make nums similar to target. The test cases are generated such that nums can always be similar to target.



Example 1:

Input: nums = [8,12,6], target = [2,14,10]
Output: 2
Explanation: It is possible to make nums similar to target in two operations:
- Choose i = 0 and j = 2, nums = [10,12,4].
- Choose i = 1 and j = 2, nums = [10,14,2].
It can be shown that 2 is the minimum number of operations needed.
Example 2:

Input: nums = [1,2,5], target = [4,1,3]
Output: 1
Explanation: We can make nums similar to target in one operation:
- Choose i = 1 and j = 2, nums = [1,4,3].
Example 3:

Input: nums = [1,1,1,1,1], target = [1,1,1,1,1]
Output: 0
Explanation: The array nums is already similiar to target.


Constraints:

n == nums.length == target.length
1 <= n <= 105
1 <= nums[i], target[i] <= 106
It is possible to make nums similar to target.


################################################################

6217. 使数组相似的最少操作次数


给你两个正整数数组 nums 和 target ，两个数组长度相等。

在一次操作中，你可以选择两个 不同 的下标 i 和 j ，其中 0 <= i, j < nums.length ，并且：

令 nums[i] = nums[i] + 2 且
令 nums[j] = nums[j] - 2 。
如果两个数组中每个元素出现的频率相等，我们称两个数组是 相似 的。

请你返回将 nums 变得与 target 相似的最少操作次数。测试数据保证 nums 一定能变得与 target 相似。


示例 1：

输入：nums = [8,12,6], target = [2,14,10]
输出：2
解释：可以用两步操作将 nums 变得与 target 相似：
- 选择 i = 0 和 j = 2 ，nums = [10,12,4] 。
- 选择 i = 1 和 j = 2 ，nums = [10,14,2] 。
2 次操作是最少需要的操作次数。


示例 2：

输入：nums = [1,2,5], target = [4,1,3]
输出：1
解释：一步操作可以使 nums 变得与 target 相似：
- 选择 i = 1 和 j = 2 ，nums = [1,4,3] 。


示例 3：

输入：nums = [1,1,1,1,1], target = [1,1,1,1,1]
输出：0
解释：数组 nums 已经与 target 相似。


提示：

n == nums.length == target.length
1 <= n <= 105
1 <= nums[i], target[i] <= 106
nums 一定可以变得与 target 相似


"""

"""
"""


"""

作者：小羊肖恩
链接：https://leetcode.cn/circle/discuss/uO4WuN/view/CUy95z/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


注意到，奇数只能变成奇数，偶数只能变成偶数。

分别考虑奇数数组和目标的奇数数组以及偶数数组和目标的偶数数组，一定是维持当前的顺序找目标更优。（否则总距离会更长）

而每一次进行操作都可以同时使得两个数更接近与自身的目标，因此，距离目标的总差值每次会减少 44，所以我们只需要计算总差值除以 44 的结果即可。

"""


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key=lambda x: (x % 2, x))
        target.sort(key=lambda x: (x % 2, x))
        # 前面的排序相当于对于奇数偶数进行了分类，前面为奇数，后面为偶数
        return sum(abs(x - y) for x, y in zip(nums, target)) // 4
