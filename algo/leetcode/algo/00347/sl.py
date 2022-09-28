"""

[347] Top K Frequent Elements


Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


--------------------------------------------------

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
--------------------------------------------------

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:


	1 <= nums.length <= 10⁵
	-10⁴ <= nums[i] <= 10⁴
	k is in the range [1, the number of unique elements in the array].
	It is guaranteed that the answer is unique.



Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


################################################################


347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。


示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]


示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。


"""

import sys
import inspect
import os
import unittest
from os.path import abspath, join, dirname
from typing import *

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)  # algo
parentdir = os.path.dirname(parentdir)  # leetcode
parentdir = os.path.dirname(parentdir)  # algo
sys.path.insert(0, parentdir)
# print(sys.path)


from algo.tree.builder import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        for n, c in count.items():
            if len(heap) < k:
                heappush(heap, (c, n))
            else:
                if heap[0][0] < c:
                    heapreplace(heap, (c, n))
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        return ans

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        for n, c in count.items():
            heappush(heap, (-c, n))
        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])
        return ans

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        arr = []
        for n, c in count.items():
            arr.append((c, n))
        arr.sort(reverse=True)
        return [i[1] for i in arr[:k]]


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
