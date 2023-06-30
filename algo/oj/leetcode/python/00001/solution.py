# Created by shiyang07ca at 2023/04/27 00:41
# https://leetcode.cn/problems/two-sum/

"""
1. 两数之和 (Easy)
给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该
数组中找出 **和为目标值**`target`  的那 **两个** 整数，并返
回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在
答案里不能重复出现。

你可以按任意顺序返回答案。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]

```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]

```

**提示：**

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- **只会存在一个有效答案**

**进阶：** 你可以想出一个时间复杂度小于 `O(n²)` 的算法吗？

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, n in enumerate(nums):
            if n in m:
                return [m[n], i]
            m[target - n] = i


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)
    print("output:", serialize(ans))
