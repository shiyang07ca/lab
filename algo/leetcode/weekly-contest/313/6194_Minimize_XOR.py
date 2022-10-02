"""

6194. Minimize XOR


Given two positive integers num1 and num2, find the integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.



Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.


Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.


Constraints:

1 <= num1, num2 <= 109

################################################################

# TODO
# tag: greedy, bit

6194. 最小 XOR
给你两个正整数 num1 和 num2 ，找出满足下述条件的整数 x ：

x 的置位数和 num2 相同，且
x XOR num1 的值 最小
注意 XOR 是按位异或运算。

返回整数 x 。题目保证，对于生成的测试用例， x 是 唯一确定 的。

整数的 置位数 是其二进制表示中 1 的数目。



示例 1：

输入：num1 = 3, num2 = 5
输出：3
解释：
num1 和 num2 的二进制表示分别是 0011 和 0101 。
整数 3 的置位数与 num2 相同，且 3 XOR 3 = 0 是最小的。


示例 2：

输入：num1 = 1, num2 = 12
输出：3
解释：
num1 和 num2 的二进制表示分别是 0001 和 1100 。
整数 3 的置位数与 num2 相同，且 3 XOR 1 = 2 是最小的。


提示：

1 <= num1, num2 <= 109


"""


class Solution1:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = bin(num1).replace("0b", "")
        b2 = bin(num2).replace("0b", "")

        c1 = b1.count("1")
        c2 = b2.count("1")

        arr = []
        if c1 == c2:
            return num1
        elif c1 > c2:
            # 从前向后遍历
            for b in b1:
                if b == "1" and c2:
                    arr.append("1")
                    c2 -= 1
                else:
                    arr.append("0")
            return int("".join(arr), 2)
        elif c1 < c2:
            # c 表示在 num1 开头的位置需要额外放多少个1
            c = c2 - c1
            # 从后向前遍历
            for b in b1[::-1]:
                if b == "0" and c:
                    arr.insert(0, "1")
                    c -= 1
                else:
                    arr.insert(0, b)
            for _ in range(c):
                arr.insert(0, "1")
            return int("".join(arr), 2)


"""

作者：endlesscheng
链接：https://leetcode.cn/problems/minimize-xor/solution/o1-kong-jian-fu-za-du-zuo-fa-by-endlessc-ywio/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。




贪心 + O(1) 空间复杂度做法

设 n1 为 num1 的二进制表示长度，c1 为 num1 的置位数，c2 为num2 的置位数
基本思路：
x 的置位数和 num2 相同，意味着 x 的二进制表示中有 c2 个 1， 我们需要合理分配这 c2 个 1。
为了让异或结果尽量小，这些 1 应当从高位到地位匹配 num1 中的 1；如果匹配完了还有多余的 1，
那么就从低位到高位把 0 改成 1。

分类讨论：
  - 如果 c2 >= n1, x 只能是 2 ** c2 - 1, 任何其他方案都会使异或结果变大
  - 如果 c2 = c1, 那么 x = num1
  - 如果 c2 < c1, 那么将 num1 的最低的 c1 - c2 个 1 变成 0， 其结果就是 x
  - 如果 c2 > c1, 那么将 num1 的最低的 c2 - c1 个 0 变成 1， 其结果就是 x

"""


class Solution2:
    def minimizeXor(self, num1: int, num2: int) -> int:
        c2 = num2.bit_count()
        if c2 >= num1.bit_length():
            return (1 << c2) - 1
        c1 = num1.bit_count()
        # c2 < c1, 把 num1 最低的 c1-c2 个1变成0
        # x 的 lowbit  ====> x & -x
        # x -= x & -x
        # or
        # x &= x - 1
        while c2 < c1:
            num1 &= num1 - 1  # 1 变成 0
            c2 += 1
        # c2 > c1, 把 num1 最低的 c2-c1 个0变成1
        # y = ~x
        # x |= y & -y
        # or
        # x |= x + 1
        while c2 > c1:
            num1 |= num1 + 1  # 0 变成 1
            c2 -= 1
        return num1


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self):
        # self.sl = Solution1()
        self.sl = Solution2()

    def test_sl(self):
        num1 = 3
        num2 = 5
        self.assertEqual(
            self.sl.minimizeXor(num1, num2),
            3,
        )

        num1 = 1
        num2 = 12
        self.assertEqual(
            self.sl.minimizeXor(num1, num2),
            3,
        )

        num1 = 4
        num2 = 12
        self.assertEqual(
            self.sl.minimizeXor(num1, num2),
            5,
        )

        num1 = 6
        num2 = 12
        self.assertEqual(
            self.sl.minimizeXor(num1, num2),
            6,
        )

        num1 = 25
        num2 = 72
        self.assertEqual(
            self.sl.minimizeXor(num1, num2),
            24,
        )

        num1 = 65
        num2 = 84
        self.assertEqual(
            self.sl.minimizeXor(num1, num2),
            67,
        )


if __name__ == "__main__":
    unittest.main()
