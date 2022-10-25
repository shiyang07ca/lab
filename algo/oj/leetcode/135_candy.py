"""

135. 分发糖果
n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。



示例 1：

输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。


示例 2：

输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。


提示：

n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104

"""

from typing import List


class Solution:
    def brute(self, ratings):
        ans = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i - 1] and ans[i] == ans[i - 1]:
                ans[i - 1] += 1
                for j in range(i - 1, 0, -1):
                    if ratings[j] >= ratings[j - 1]:  # 剪枝
                        break
                    # ratings[j] < ratings[j - 1]
                    elif ans[j] >= ans[j - 1]:
                        ans[j - 1] += 1
            elif ratings[i] > ratings[i - 1]:
                ans[i] = ans[i - 1] + 1

        return sum(ans)

    def greedy(self, ratings):
        left = [1] * len(ratings)
        right = [1] * len(ratings)
        # 上坡
        # 从第二个元素遍历到末尾，如果当前元素分数大于前一个分数，
        # 就把前一个糖果数 + 1 作为当前元素糖果数
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # 下坡
        # 从倒数第二个元素遍历到末尾，如果当前元素分数大于后一个分数，
        # 就把后一个糖果数 + 1 作为当前元素糖果数
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1

        # 左右数组每个位置的最大值，作为当前位置的糖果数
        return sum([max(left[i], right[i]) for i in range(0, len(left))])

    def candy(self, ratings: List[int]) -> int:
        # return self.brute(ratings)
        return self.greedy(ratings)


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def random_check(self):
        import random

        # L = 1000
        for _ in range(1000):
            random_l = [random.randrange(100) for _ in range(random.randrange(100))]
            # print(self.sl.burte(random_l))
            self.assertEqual(self.sl.brute(random_l), self.sl.greedy(random_l))

    def test_sl(self):
        ratings = [1, 0, 2]
        self.assertEqual(self.sl.candy(ratings), 5)

        ratings = [1, 2, 2]
        self.assertEqual(self.sl.candy(ratings), 4)

        ratings = [1, 2, 2, 1, 3]
        self.assertEqual(self.sl.candy(ratings), 8)

        ratings = [0, 2, 3, 4, 5]
        self.assertEqual(self.sl.candy(ratings), 15)

        ratings = [1, 2, 2, 2, 3, 2]
        self.assertEqual(self.sl.candy(ratings), 8)

        ratings = [1, 2, 2, 3, 3, 3, 2]
        self.assertEqual(self.sl.candy(ratings), 10)

        ratings = [3, 3, 2, 1, 2]
        self.assertEqual(self.sl.candy(ratings), 9)

        ratings = [1, 3, 2, 2, 1]
        self.assertEqual(self.sl.candy(ratings), 7)

        L = 1000
        ratings = list(range(L, 0, -1))
        self.assertEqual(self.sl.candy(ratings), sum(list(range(1, len(ratings) + 1))))

        self.random_check()


if __name__ == "__main__":
    unittest.main()
