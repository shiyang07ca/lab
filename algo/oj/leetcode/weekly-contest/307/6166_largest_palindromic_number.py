"""


给你一个仅由数字（0 - 9）组成的字符串 num 。

请你找出能够使用 num 中数字形成的 最大回文 整数，并以字符串形式返回。该整数不含 前导零 。

注意：

你 无需 使用 num 中的所有数字，但你必须使用 至少 一个数字。
数字可以重新排序。


示例 1：

输入：num = "444947137"
输出："7449447"
解释：
从 "444947137" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
可以证明 "7449447" 是能够形成的最大回文整数。


示例 2：

输入：num = "00009"
输出："9"
解释：
可以证明 "9" 能够形成的最大回文整数。
注意返回的整数不应含前导零。


提示：

1 <= num.length <= 105
num 由数字（0 - 9）组成

"""


class Solution:
    def largestPalindromic(self, num: str) -> str:
        nmap = {}
        nums = sorted([n for n in num], reverse=True)
        for n in num:
            if n in nmap:
                nmap[n] += 1
            else:
                nmap[n] = 1

        nmap = dict(sorted(nmap.items(), reverse=True))
        #         print(nmap)
        #         print(nums)

        pre = ""
        mid = ""
        for n in nums:
            #             print('pre: ', pre)
            if (n != "0" or len(pre) != 0) and n in nmap and nmap[n] >= 2:
                pre += str(n)
                nmap[n] -= 2
        #         print(pre)
        for n, count in nmap.items():
            if nmap[n] >= 1:
                mid = str(n)
                break

        #         print(pre + mid + pre[::-1])

        return pre + mid + pre[::-1]
