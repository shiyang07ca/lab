"""

6222. Minimum Addition to Make Integer Beautiful

You are given two positive integers n and target.

An integer is considered beautiful if the sum of its digits is less than or equal to target.

Return the minimum non-negative integer x such that n + x is beautiful. The input will be generated such that it is always possible to make n beautiful.



Example 1:

Input: n = 16, target = 6
Output: 4
Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7. After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. It can be shown that we can not make n beautiful with adding non-negative integer less than 4.

Example 2:

Input: n = 467, target = 6
Output: 33
Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17. After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. It can be shown that we can not make n beautiful with adding non-negative integer less than 33.

Example 3:

Input: n = 1, target = 1
Output: 0
Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.


Constraints:

1 <= n <= 1012
1 <= target <= 150
The input will be generated such that it is always possible to make n beautiful.

################################################################

# TODO
# tag: greedy, simulation

6222. 美丽整数的最小增量


给你两个正整数 n 和 target 。

如果某个整数每一位上的数字相加小于或等于 target ，则认为这个整数是一个 美丽整数 。

找出并返回满足 n + x 是 美丽整数 的最小非负整数 x 。生成的输入保证总可以使 n 变成一个美丽整数。



示例 1：

输入：n = 16, target = 6
输出：4
解释：最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。


示例 2：

输入：n = 467, target = 6
输出：33
解释：最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。


示例 3：

输入：n = 1, target = 1
输出：0
解释：最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。


提示：

1 <= n <= 10^12
1 <= target <= 150
生成的输入保证总可以使 n 变成一个美丽整数。


"""


"""

作者：endlesscheng
链接：https://leetcode.cn/problems/minimum-addition-to-make-integer-beautiful/solution/tan-xin-by-endlesscheng-f7e4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


基本思路是，不断 +1+1 直到产生进位，就可能让数位和变小。

代码实现时，可以直接计算每个数位进位后的结果。

比如 467467，十位数进位为 470470，百位数进位为 500500，千位数进位为 10001000（这一点在 \textit{target}=1target=1 时尤为重要）。


"""


class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        tail = 1
        while True:
            m = x = n + (tail - n % tail) % tail  # 进位后的数字
            s = 0
            while x:
                s += x % 10
                x //= 10
            if s <= target:
                return m - n
            tail *= 10
