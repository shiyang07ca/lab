"""

[1825] Finding MK Average


You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:


	If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
	Remove the smallest k elements and the largest k elements from the container.
	Calculate the average value for the rest of the elements rounded down to the nearest integer.


Implement the MKAverage class:


	MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
	void addElement(int num) Inserts a new element num into the stream.
	int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.



Example 1:


Input
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
Output
[null, null, null, -1, null, 3, null, null, null, 5]

Explanation
MKAverage obj = new MKAverage(3, 1);
obj.addElement(3);        // current elements are [3]
obj.addElement(1);        // current elements are [3,1]
obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements exist.
obj.addElement(10);       // current elements are [3,1,10]
obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
                          // After removing smallest and largest 1 element the container will be [3].
                          // The average of [3] equals 3/1 = 3, return 3
obj.addElement(5);        // current elements are [3,1,10,5]
obj.addElement(5);        // current elements are [3,1,10,5,5]
obj.addElement(5);        // current elements are [3,1,10,5,5,5]
obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
                          // After removing smallest and largest 1 element the container will be [5].
                          // The average of [5] equals 5/1 = 5, return 5



Constraints:


	3 <= m <= 10⁵
	1 <= k*2 < m
	1 <= num <= 10⁵
	At most 10⁵ calls will be made to addElement and calculateMKAverage.

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

from sortedcontainers import SortedList


from sortedcontainers import SortedList


class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.sum2 = 0
        self.s1, self.s2, self.s3 = SortedList(), SortedList(), SortedList()
        self.q = deque()

    def addElement(self, num: int) -> None:
        self.q.append(num)
        if len(self.q) <= self.m:
            self.s2.add(num)
            self.sum2 += num
            if len(self.q) == self.m:
                while len(self.s1) < self.k:
                    s2mi = self.s2.pop(0)
                    self.sum2 -= s2mi
                    self.s1.add(s2mi)
                while len(self.s3) < self.k:
                    s2ma = self.s2.pop(-1)
                    self.sum2 -= s2ma
                    self.s3.add(s2ma)
        elif len(self.q) == self.m + 1:
            if num < self.s1[-1]:
                self.s1.add(num)
                s1ma = self.s1.pop(-1)
                self.s2.add(s1ma)
                self.sum2 += s1ma
            elif num > self.s3[0]:
                self.s3.add(num)
                s3mi = self.s3.pop(0)
                self.s2.add(s3mi)
                self.sum2 += s3mi
            else:
                self.s2.add(num)
                self.sum2 += num

            x = self.q.popleft()
            if x in self.s2:
                self.s2.remove(x)
                self.sum2 -= x
            elif x in self.s1:
                self.s1.remove(x)
                s2mi = self.s2.pop(0)
                self.sum2 -= s2mi
                self.s1.add(s2mi)
            elif x in self.s3:
                self.s3.remove(x)
                s2ma = self.s2.pop(-1)
                self.sum2 -= s2ma
                self.s3.add(s2ma)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        else:
            return self.sum2 // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()


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
