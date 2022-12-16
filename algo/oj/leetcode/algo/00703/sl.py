"""

[703] Kth Largest Element in a Stream


Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:


	KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
	int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.



Example 1:


Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8



Constraints:


	1 <= k <= 10⁴
	0 <= nums.length <= 10⁴
	-10⁴ <= nums[i] <= 10⁴
	-10⁴ <= val <= 10⁴
	At most 10⁴ calls will be made to add.
	It is guaranteed that there will be at least k elements in the array when you search for the kth element.

################################################################

# TODO
# tag: heap

703. 数据流中的第 K 大元素

设计一个找到数据流中第 `k` 大元素的类（class）。注意是排序后的第 `k` 大元素，不是第 `k` 个不同的元素。

请实现 `KthLargest` 类：

-   `KthLargest(int k, int[] nums)` 使用整数 `k` 和整数流 `nums` 初始化对象。
-   `int add(int val)` 将 `val` 插入数据流 `nums` 后，返回当前数据流中第 `k` 大的元素。



**示例：**

```txt
输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

**提示：**

-   `1 <= k <= 10^4`
-   `0 <= nums.length <= 10^4`
-   `-10^4 <= nums[i] <= 10^4`
-   `-10^4 <= val <= 10^4`
-   最多调用 `add` 方法 `10^4` 次
-   题目数据保证，在查找第 `k` 大元素时，数组中至少有 `k` 个元素
"""

import sys
import inspect
import os
import unittest

from itertools import *
from collections import *
from copy import *
from typing import *
from math import *

from os.path import abspath, join, dirname

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # oj
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *

"""
维护一个大小为 k 的小根堆，这个堆始终保存数据流中前 k 大的元素，那么堆顶就是第 k
大的元素
"""

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = nums
        self.k = k
        heapify(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)
        while len(self.h) > self.k:
            heappop(self.h)

        return self.h[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        self.assertEqual(
            self.sl,
            None,
        )


if __name__ == "__main__":
    unittest.main()
