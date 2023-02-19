"""

[1792] Maximum Average Pass Ratio


There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.


Example 2:


Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485



Constraints:


	1 <= classes.length <= 10⁵
	classes[i].length == 2
	1 <= passi <= totali <= 10⁵
	1 <= extraStudents <= 10⁵

################################################################

# TODO
# tag: Greedy

1792. 最大平均通过率

一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 classes ，其中 classes[i] = [passi, totali] ，表示你提前知道了第 i 个班级总共有 totali 个学生，其中只有 passi 个学生可以通过考试。

给你一个整数 extraStudents ，表示额外有 extraStudents 个聪明的学生，他们 一定 能通过任何班级的期末考。你需要给这 extraStudents 个学生每人都安排一个班级，使得 所有 班级的 平均 通过率 最大 。

一个班级的 通过率 等于这个班级通过考试的学生人数除以这个班级的总人数。平均通过率 是所有班级的通过率之和除以班级数目。

请你返回在安排这 extraStudents 个学生去对应班级后的 最大 平均通过率。与标准答案误差范围在 10-5 以内的结果都会视为正确结果。



示例 1：

输入：classes = [[1,2],[3,5],[2,2]], extraStudents = 2
输出：0.78333
解释：你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。


示例 2：

输入：classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
输出：0.53485


提示：

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105

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

from heapq import *


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for i, (a, b) in enumerate(classes):
            d = (a + 1) / (b + 1) - a / b
            heappush(h, (-d, i))

        for _ in range(extraStudents):
            _, i = h[0]
            a, b = classes[i]
            new_d = (a + 2) / (b + 2) - (a + 1) / (b + 1)
            heapreplace(h, (-new_d, i))
            classes[i] = [a + 1, b + 1]

        ans = 0
        for a, b in classes:
            ans += a / b

        return ans / len(classes)


"""
https://leetcode.cn/problems/maximum-average-pass-ratio/solution/python3javacgo-yi-ti-yi-jie-you-xian-dui-qrmo/


设一个班级当前通过率为 a / b，每安排油罐车聪明学生到一个班级，那么班级的通过率就
会增加 (a + 1)/(b + 1) - a/b

维护一个大根堆，堆中存储每个班级的通过率增量
进行 extraStudents 次操作，每次从堆顶取出一个班级，将这个班级的人数和通过人数都
加 1，然后将这个班级的通过率增量重新计算并放回堆中。重复这个过程，直到将所有的学
生都分配完毕。


最后，我们将所有班级的通过率求和，然后除以班级数目，即为答案。

"""


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = [(a / b - (a + 1) / (b + 1), a, b) for a, b in classes]
        heapify(h)
        for _ in range(extraStudents):
            _, a, b = heappop(h)
            a, b = a + 1, b + 1
            heappush(h, (a / b - (a + 1) / (b + 1), a, b))
        return sum(v[1] / v[2] for v in h) / len(classes)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sl = Solution()

    def test_sl(self):

        classes = [[1, 2], [3, 5], [2, 2]]
        extraStudents = 2

        # 0.78333
        print(self.sl.maxAverageRatio(classes, extraStudents))

        classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
        extraStudents = 4
        # 0.53485
        print(self.sl.maxAverageRatio(classes, extraStudents))


if __name__ == "__main__":
    unittest.main()
