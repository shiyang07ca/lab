"""

[1691] Maximum Height by Stacking Cuboids


Given n cuboids where the dimensions of the ith cuboid is cuboids[i] = [widthi, lengthi, heighti] (0-indexed). Choose a subset of cuboids and place them on each other.

You can place cuboid i on cuboid j if widthi <= widthj and lengthi <= lengthj and heighti <= heightj. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return the maximum height of the stacked cuboids.


Example 1:




Input: cuboids = [[50,45,20],[95,37,53],[45,23,12]]
Output: 190
Explanation:
Cuboid 1 is placed on the bottom with the 53x37 side facing down with height 95.
Cuboid 0 is placed next with the 45x20 side facing down with height 50.
Cuboid 2 is placed next with the 23x12 side facing down with height 45.
The total height is 95 + 50 + 45 = 190.


Example 2:


Input: cuboids = [[38,25,45],[76,35,3]]
Output: 76
Explanation:
You can't place any of the cuboids on the other.
We choose cuboid 1 and rotate it so that the 35x3 side is facing down and its height is 76.


Example 3:


Input: cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
Output: 102
Explanation:
After rearranging the cuboids, you can see that all cuboids have the same dimension.
You can place the 11x7 side down on all cuboids so their heights are 17.
The maximum height of stacked cuboids is 6 * 17 = 102.



Constraints:


	n == cuboids.length
	1 <= n <= 100
	1 <= widthi, lengthi, heighti <= 100

################################################################

# TODO

1691. 堆叠长方体的最大高度
给你 n 个长方体 cuboids ，其中第 i 个长方体的长宽高表示为 cuboids[i] = [widthi, lengthi, heighti]（下标从 0 开始）。请你从 cuboids 选出一个 子集 ，并将它们堆叠起来。

如果 widthi <= widthj 且 lengthi <= lengthj 且 heighti <= heightj ，你就可以将长方体 i 堆叠在长方体 j 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。

返回 堆叠长方体 cuboids 可以得到的 最大高度 。



示例 1：



输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
输出：190
解释：
第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
总高度是 95 + 50 + 45 = 190 。


示例 2：

输入：cuboids = [[38,25,45],[76,35,3]]
输出：76
解释：
无法将任何长方体放在另一个上面。
选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。


示例 3：

输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
输出：102
解释：
重新排列长方体后，可以看到所有长方体的尺寸都相同。
你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
堆叠长方体的最大高度为 6 * 17 = 102 。


提示：

n == cuboids.length
1 <= n <= 100
1 <= widthi, lengthi, heighti <= 100

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
作者：endlesscheng
链接：https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/solution/tu-jie-suan-fa-you-hua-xiang-xi-zheng-mi-b6fq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

一个结论
设两个长方体 A[w1, l1, h1], B = [w2, l2, h2]，
其中 w1 <= l1 <= h1 且 w2 <= l2 <= h2
那么： A 可以堆在 B 上，当且仅当 w1 <= w2 且 l1 <= l2 且 h1 <= h2



定义 f[i] 表示考虑排序后的前 i 个长方体，将第 i 个长方体置于底部时的最大堆叠高度
        f[i] = max(f[j]) + hi    j < i 且 lj <= li 且 hj <= hi

答案为 max(f)


相似题目
LC300. 最长递增子序列 https://leetcode.cn/problems/longest-increasing-subsequence/
LC354. 俄罗斯套娃信封问题 https://leetcode.cn/problems/russian-doll-envelopes/

"""


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for c in cuboids:
            c.sort()
        cuboids.sort()
        f = [0] * len(cuboids)
        for i, (_, l2, h2) in enumerate(cuboids):
            for j, (_, l1, h1) in enumerate(cuboids[:i]):
                if l1 <= l2 and h1 <= h2:  # 排序后，w1 <= w2 恒成立
                    f[i] = max(f[i], f[j])  # cuboids[j] 可以堆在 cuboids[i] 上
            f[i] += h2
        return max(f)


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
