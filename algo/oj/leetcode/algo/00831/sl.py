"""

[831] Masking Personal Information


You are given a personal information string s, representing either an email address or a phone number. Return the masked personal information using the below rules.

Email address:

An email address is:


	A name consisting of uppercase and lowercase English letters, followed by
	The '@' symbol, followed by
	The domain consisting of uppercase and lowercase English letters with a dot '.' somewhere in the middle (not the first or last character).


To mask an email:


	The uppercase letters in the name and domain must be converted to lowercase letters.
	The middle letters of the name (i.e., all but the first and last letters) must be replaced by 5 asterisks "*****".


Phone number:

A phone number is formatted as follows:


	The phone number contains 10-13 digits.
	The last 10 digits make up the local number.
	The remaining 0-3 digits, in the beginning, make up the country code.
	Separation characters from the set {'+', '-', '(', ')', ' '} separate the above digits in some way.


To mask a phone number:


	Remove all separation characters.
	The masked phone number should have the form:

		"***-***-XXXX" if the country code has 0 digits.
		"+*-***-***-XXXX" if the country code has 1 digit.
		"+**-***-***-XXXX" if the country code has 2 digits.
		"+***-***-***-XXXX" if the country code has 3 digits.


	"XXXX" is the last 4 digits of the local number.



Example 1:


Input: s = "LeetCode@LeetCode.com"
Output: "l*****e@leetcode.com"
Explanation: s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.


Example 2:


Input: s = "AB@qq.com"
Output: "a*****b@qq.com"
Explanation: s is an email address.
The name and domain are converted to lowercase, and the middle of the name is replaced by 5 asterisks.
Note that even though "ab" is 2 characters, it still must have 5 asterisks in the middle.


Example 3:


Input: s = "1(234)567-890"
Output: "***-***-7890"
Explanation: s is a phone number.
There are 10 digits, so the local number is 10 digits and the country code is 0 digits.
Thus, the resulting masked number is "***-***-7890".



Constraints:


	s is either a valid email or a phone number.
	If s is an email:

		8 <= s.length <= 40
		s consists of uppercase and lowercase English letters and exactly one '@' symbol and '.' symbol.


	If s is a phone number:

		10 <= s.length <= 20
		s consists of digits, spaces, and the symbols '(', ')', '-', and '+'.


################################################################

# TODO
# tag: dp, Prefix Sum

813. 最大平均值和的分组
给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个相邻的非空子数组 。 分数 由每个子数组内的平均值的总和构成。

注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。

返回我们所能得到的最大 分数 是多少。答案误差在 10-6 内被视为是正确的。


示例 1:

输入: nums = [9,1,2,3,9], k = 3
输出: 20.00000
解释:
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 nums 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.


示例 2:

输入: nums = [1,2,3,4,5,6,7], k = 4
输出: 20.50000


提示:

1 <= nums.length <= 100
1 <= nums[i] <= 104
1 <= k <= nums.length


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

TODO

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/largest-sum-of-averages/solution/zui-da-ping-jun-zhi-he-de-fen-zu-by-leet-09xt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


"""


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # f[i][j] 表示 [0,i-1] 范围数组分成 j 个数组的最大平均值
        # return f[n][k]
        N = len(nums)
        pre = list(accumulate(nums, initial=0))
        f = [[0.0] * (k + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            f[i][1] = pre[i] / i

        for j in range(2, k + 1):
            for i in range(j, N + 1):
                for x in range(j - 1, i):
                    f[i][j] = max(f[i][j], f[x][j - 1] + (pre[i] - pre[x]) / (i - x))

        return f[N][k]


"""

作者：lcbin
链接：https://leetcode.cn/problems/largest-sum-of-averages/solution/by-lcbin-5efy/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

我们可以先预处理得到前缀和数组 s，方便快速得到子数组的和。

然后设计一个函数 dfs(i,k)，表示从数组下标 i 开始，最多分成 k 组的最大平均值和。
答案即为 dfs(0, k)

函数 dfs(i, k) 的执行逻辑如下：

* 当 i=n 时，表示已经遍历到数组末尾，此时返回 0。
* 当 k=1 时，表示只剩下一组，此时返回从下标 i 开始到数组末尾的平均值。
* 否则，我们在 [i,..n−1] 的范围内枚举分组的结束位置 j，计算从下标 i 到下标 j 的
平均值，以及从下标 j+1 开始，最多分成 k-1 组的最大平均值和。取其中的最大值作为答
案。

为了避免重复计算，我们可以用数组 f 记忆化函数 dfs(i, k) 的返回值。

"""


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def dfs(i, k):
            if i == n:
                return 0
            if k == 1:
                return (s[-1] - s[i]) / (n - i)
            ans = 0
            for j in range(i, n):
                t = (s[j + 1] - s[i]) / (j - i + 1) + dfs(j + 1, k - 1)
                ans = max(ans, t)
            return ans

        n = len(nums)
        s = list(accumulate(nums, initial=0))
        return dfs(0, k)


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
