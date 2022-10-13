"""

[769] Max Chunks To Make Sorted


You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.


Example 1:


Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.


Example 2:


Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.



Constraints:


	n == arr.length
	1 <= n <= 10
	0 <= arr[i] < n
	All the elements of arr are unique.

################################################################


769. 最多能完成排序的块
给定一个长度为 n 的整数数组 arr ，它表示在 [0, n - 1] 范围内的整数的排列。

我们将 arr 分割成若干 块 (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。



示例 1:

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。


示例 2:

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。


提示:

n == arr.length
1 <= n <= 10
0 <= arr[i] < n
arr 中每个元素都 不同

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

from sortedcontainers import SortedList


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        arr1 = sorted(arr)

        s = [None] * len(arr)
        for i in range(len(arr)):
            tmp = set()
            for j in range(0, i + 1):
                tmp.add(tuple(arr1[j : i + 1]))
            s[i] = tmp

        tmp = SortedList()
        ans = 0
        for i, n in enumerate(arr):
            tmp.add(n)
            if tuple(tmp) in s[i]:
                ans += 1
                tmp = SortedList()
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):
        arr = [4, 3, 2, 1, 0]
        self.assertEqual(
            self.sl.maxChunksToSorted(arr),
            1,
        )

        arr = [1, 0, 2, 3, 4]
        self.assertEqual(
            self.sl.maxChunksToSorted(arr),
            4,
        )


if __name__ == "__main__":
    unittest.main()
