# Created by shiyang07ca at 2023/04/26 21:58
# https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/

"""
1031. 两个非重叠子数组的最大和 (Medium)
给你一个整数数组 `nums` 和两个整数 `firstLen` 和 `secondLen`
，请你找出并返回两个非重叠 **子数组** 中元素的最大和，长度分
别为 `firstLen` 和 `secondLen` 。

长度为 `firstLen` 的子数组可以出现在长为 `secondLen` 的子数
组之前或之后，但二者必须是不重叠的。

子数组是数组的一个 **连续** 部分。

**示例 1：**

```
输入：nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen =
2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。

```

**示例 2：**

```
输入：nums = [3,8,1,3,2,1,8,9,0], firstLen = 3, secondLen =
2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。

```

**示例 3：**

```
输入：nums = [2,1,5,6,0,9,5,0,3,8], firstLen = 4, secondLen
= 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为
3。

```

**提示：**

- `1 <= firstLen, secondLen <= 1000`
- `2 <= firstLen + secondLen <= 1000`
- `firstLen + secondLen <= nums.length <= 1000`
- `0 <= nums[i] <= 1000`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

from itertools import accumulate

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], a: int, b: int) -> int:
        nums = list(accumulate(nums, initial=0))
        ans = 0
        n = len(nums)
        for i in range(n):
            if i + a >= n:
                break
            da = nums[i + a] - nums[i]
            for j in range(i + a, n):
                if j + b >= n:
                    break
                db = nums[j + b] - nums[j]
                ans = max(ans, da + db)
        for i in range(n):
            if i + b >= n:
                break
            db = nums[i + b] - nums[i]
            for j in range(i + b, n):
                if j + a >= n:
                    break
                da = nums[j + a] - nums[j]
                ans = max(ans, da + db)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    firstLen: int = deserialize("int", read_line())
    secondLen: int = deserialize("int", read_line())
    ans = Solution().maxSumTwoNoOverlap(nums, firstLen, secondLen)
    print("output:", serialize(ans))
